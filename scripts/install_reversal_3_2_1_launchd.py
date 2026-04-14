from __future__ import annotations

import argparse
import plistlib
import subprocess
from pathlib import Path


LABEL = "com.randomwalkhan.reversal-3-2-1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the Reversal 3.2.1 launchd schedule.")
    parser.add_argument("--project-dir", type=Path, default=Path.cwd().resolve())
    parser.add_argument("--python-bin", default="/Users/mac/miniconda3/envs/quant/bin/python")
    parser.add_argument("--start-immediately", action="store_true")
    return parser.parse_args()


def build_schedule() -> list[dict[str, int]]:
    weekday_entries = []
    five_minute_slots = [(hour, minute) for hour in range(0, 24) for minute in range(0, 60, 5)]
    for weekday in [1, 2, 3, 4, 5]:
        for hour, minute in five_minute_slots:
            weekday_entries.append({"Weekday": weekday, "Hour": hour, "Minute": minute})
    return weekday_entries


def main() -> None:
    args = parse_args()
    launch_agents_dir = Path.home() / "Library" / "LaunchAgents"
    launch_agents_dir.mkdir(parents=True, exist_ok=True)

    plist_path = launch_agents_dir / f"{LABEL}.plist"
    log_dir = args.project_dir / "results" / "reversal_3_2_1_live"
    log_dir.mkdir(parents=True, exist_ok=True)

    plist_data = {
        "Label": LABEL,
        "ProgramArguments": [
            args.python_bin,
            str((args.project_dir / "reversal_3_2_1_live.py").resolve()),
        ],
        "WorkingDirectory": str(args.project_dir),
        "StandardOutPath": str((log_dir / "launchd.out.log").resolve()),
        "StandardErrorPath": str((log_dir / "launchd.err.log").resolve()),
        "StartCalendarInterval": build_schedule(),
        "RunAtLoad": False,
        "EnvironmentVariables": {
            "PYTHONUNBUFFERED": "1",
        },
    }

    with plist_path.open("wb") as fh:
        plistlib.dump(plist_data, fh, sort_keys=False)

    subprocess.run(["launchctl", "bootout", f"gui/{subprocess.check_output(['id', '-u'], text=True).strip()}", str(plist_path)], check=False)
    subprocess.run(["launchctl", "bootstrap", f"gui/{subprocess.check_output(['id', '-u'], text=True).strip()}", str(plist_path)], check=True)
    subprocess.run(["launchctl", "enable", f"gui/{subprocess.check_output(['id', '-u'], text=True).strip()}/{LABEL}"], check=False)

    if args.start_immediately:
        subprocess.run(["launchctl", "kickstart", "-k", f"gui/{subprocess.check_output(['id', '-u'], text=True).strip()}/{LABEL}"], check=False)

    print(f"Installed launchd service -> {plist_path}")
    print("Scheduled PT run times:")
    print("Every 5 minutes on weekdays. Regular-session logic remains unchanged; off-hours scans only act on open share-fallback positions.")


if __name__ == "__main__":
    main()
