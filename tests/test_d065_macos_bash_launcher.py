"""D-065 launcher checks with fake dialogs/controller; no formal assets are touched."""

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


LAUNCHER = Path(__file__).resolve().parents[1] / "Black_Lady_Ingest.command"
SOURCE_REFERENCE = "P1 Character Gap Production / PO approved via main Chat / one-click ingest"


class LauncherTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "scripts").mkdir()
        self.source = self.root / "CHAR_TEST_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png"
        self.source.write_bytes(b"fake PNG for launcher test")
        self.args_out = self.root / "controller_args.json"

        fake_osascript = self.root / "osascript"
        fake_osascript.write_text("""#!/bin/sh
if [ "${1-}" = "-" ]; then
    [ "$FAKE_REPLACE_APPROVED" = YES ]
    exit $?
fi
script=$(cat)
case "$script" in
    *"choose file"*)
        [ "$FAKE_SELECT_APPROVED" = YES ] || exit 1
        printf '%s\\n' "$FAKE_SELECTED_PNG"
        ;;
    *) [ "$FAKE_PO_APPROVED" = YES ] ;;
esac
""")
        fake_osascript.chmod(0o755)

        launcher = LAUNCHER.read_text()
        self.assertEqual(launcher.count("/usr/bin/osascript"), 3)
        (self.root / LAUNCHER.name).write_text(
            launcher.replace("/usr/bin/osascript", str(fake_osascript))
        )
        (self.root / "scripts" / "automatic_ingest_controller_v0_1.py").write_text(
            "import json, os, sys\n"
            "from pathlib import Path\n"
            "if '--inspect-current' in sys.argv:\n"
            "    print(json.dumps({'status': os.environ['FAKE_CURRENT_STATUS'], "
            "'old_filename': 'old.png', 'new_filename': 'new.png', "
            "'migration_only': False}))\n"
            "else:\n"
            "    Path(os.environ['FAKE_ARGS_OUT']).write_text(json.dumps(sys.argv[1:]))\n"
        )

    def run_launcher(self, status="NO_CURRENT", **overrides):
        env = os.environ.copy()
        env.update({
            "FAKE_CURRENT_STATUS": status,
            "FAKE_PO_APPROVED": "YES",
            "FAKE_SELECT_APPROVED": "YES",
            "FAKE_REPLACE_APPROVED": "YES",
            "FAKE_SELECTED_PNG": str(self.source),
            "FAKE_ARGS_OUT": str(self.args_out),
        })
        env.update(overrides)
        return subprocess.run(
            ["/bin/bash", str(self.root / LAUNCHER.name)],
            input="\n", text=True, capture_output=True, env=env, timeout=10,
        )

    def expected_args(self):
        return [
            "--source", str(self.source), "--from-filename",
            "--authority", "AUXILIARY", "--resolver-usage", "DEFAULT",
            "--task-id", "P0.2-03", "--source-reference", SOURCE_REFERENCE,
            "--po-approved",
        ]

    def test_no_current_uses_plain_ingest_under_macos_bash(self):
        result = self.run_launcher()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("unbound variable", result.stdout + result.stderr)
        self.assertEqual(json.loads(self.args_out.read_text()), self.expected_args())

    def test_current_found_passes_explicit_supersede_flag(self):
        result = self.run_launcher("CURRENT_FOUND")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(self.args_out.read_text()),
                         self.expected_args() + ["--supersede-current"])

    def test_product_owner_decline_blocks_before_inspection(self):
        result = self.run_launcher(FAKE_PO_APPROVED="NO")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Product Owner confirmation was not given", result.stdout)
        self.assertFalse(self.args_out.exists())

    def test_file_selection_cancel_blocks_before_inspection(self):
        result = self.run_launcher(FAKE_SELECT_APPROVED="NO")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("No PNG was selected", result.stdout)
        self.assertFalse(self.args_out.exists())

    def test_replacement_cancel_blocks_before_ingest(self):
        result = self.run_launcher("CURRENT_FOUND", FAKE_REPLACE_APPROVED="NO")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Current replacement was cancelled", result.stdout)
        self.assertFalse(self.args_out.exists())


if __name__ == "__main__":
    unittest.main()
