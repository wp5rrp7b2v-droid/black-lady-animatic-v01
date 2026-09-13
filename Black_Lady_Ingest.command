#!/bin/bash
set -u

cd "$(dirname "$0")" || exit 1
trap 'printf "\nPress Enter to close"; read -r _' EXIT

if ! /usr/bin/osascript <<'APPLESCRIPT'
set answer to display dialog "此工具仅用于已经由 Product Owner 明确批准的正式图片。是否继续入库？" buttons {"取消", "继续"} default button "取消" with icon caution
if button returned of answer is not "继续" then error number -128
APPLESCRIPT
then
    echo "INGEST BLOCKED: Product Owner confirmation was not given."
    exit 1
fi

if ! selected_png=$(/usr/bin/osascript <<'APPLESCRIPT'
POSIX path of (choose file with prompt "请选择已批准的 canonical Character PNG" of type {"public.png"})
APPLESCRIPT
); then
    echo "INGEST BLOCKED: No PNG was selected."
    exit 1
fi

if ! inspection=$(python3 -B scripts/automatic_ingest_controller_v0_1.py \
    --source "$selected_png" --from-filename --inspect-current); then
    echo "INGEST BLOCKED: Could not inspect the selected asset."
    exit 1
fi

if ! inspect_fields=$(printf '%s' "$inspection" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["status"]); print(d.get("old_filename") or ""); print(d["new_filename"]); print("YES" if d.get("migration_only") else "NO")'); then
    echo "INGEST BLOCKED: Invalid controller inspection result."
    exit 1
fi
current_status=$(printf '%s\n' "$inspect_fields" | sed -n '1p')
old_filename=$(printf '%s\n' "$inspect_fields" | sed -n '2p')
new_filename=$(printf '%s\n' "$inspect_fields" | sed -n '3p')
migration_only=$(printf '%s\n' "$inspect_fields" | sed -n '4p')

if [ "$current_status" = "CURRENT_FOUND" ]; then
    if ! /usr/bin/osascript - "$old_filename" "$new_filename" <<'APPLESCRIPT'
on run argv
    set oldName to item 1 of argv
    set newName to item 2 of argv
    set promptText to "检测到当前已有正式 CURRENT 资产：" & return & return & oldName & return & return & "本次将以：" & return & return & newName & return & return & "替换当前版本。" & return & return & "旧版本不会删除，将标记为 SUPERSEDED。" & return & return & "是否继续？"
    set answer to display dialog promptText buttons {"取消", "替换 Current"} default button "取消" with icon caution
    if button returned of answer is not "替换 Current" then error number -128
end run
APPLESCRIPT
    then
        echo "INGEST BLOCKED: Current replacement was cancelled."
        exit 1
    fi
elif [ "$current_status" != "NO_CURRENT" ] || [ "$migration_only" = "YES" ]; then
    echo "INGEST BLOCKED: Unsupported Current state."
    exit 1
fi

run_ingest() {
    if [ "$current_status" = "CURRENT_FOUND" ]; then
        python3 -B scripts/automatic_ingest_controller_v0_1.py \
            --source "$selected_png" \
            --from-filename \
            --authority AUXILIARY \
            --resolver-usage DEFAULT \
            --task-id P0.2-03 \
            --source-reference "P1 Character Gap Production / PO approved via main Chat / one-click ingest" \
            --po-approved \
            --supersede-current
    else
        python3 -B scripts/automatic_ingest_controller_v0_1.py \
            --source "$selected_png" \
            --from-filename \
            --authority AUXILIARY \
            --resolver-usage DEFAULT \
            --task-id P0.2-03 \
            --source-reference "P1 Character Gap Production / PO approved via main Chat / one-click ingest" \
            --po-approved
    fi
}

if run_ingest; then
    echo "INGEST COMPLETE"
else
    echo "INGEST BLOCKED: See the reason above."
    exit 1
fi
