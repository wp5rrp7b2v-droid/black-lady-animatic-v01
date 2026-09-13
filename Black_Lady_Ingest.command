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

if python3 -B scripts/automatic_ingest_controller_v0_1.py \
    --source "$selected_png" \
    --from-filename \
    --authority AUXILIARY \
    --resolver-usage DEFAULT \
    --task-id P0.2-03 \
    --source-reference "P1 Character Gap Production / PO approved via main Chat / one-click ingest" \
    --po-approved; then
    echo "INGEST COMPLETE"
else
    echo "INGEST BLOCKED: See the reason above."
    exit 1
fi
