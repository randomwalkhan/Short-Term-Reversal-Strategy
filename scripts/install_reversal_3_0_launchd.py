from __future__ import annotations

import argparse
import plistlib
import subprocess
from pathlib import Path


LABEL = "com.randomwalkhan.reversal-3-0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the Reversal 3.0 launchd schedule.")
    parser.add_argument("--project-dir", type=Path, default=Path.cwd().resolve())
    parser.add_argument("--python-bin", default="/Users/mac/miniconda3/envs/quant/bin/python")
    parser.add_argument("--start-immediately", action="store_true")
    return parser.parse_args()


def build_schedule() -> list[dict[str, int]]:
    weekday_entries = []
    hourly_slots = [
        (6, 30),
        (7, 30),
        (8, 30),
        (9, 30),
        (10, 30),
        (11, 30),
        (12, 0),
        (12, 30),
    ]
    for weekday in [1, 2, 3, 4, 5]:
        for hour, minute in hourly_slots:
            weekday_entries.append({"Weekday": weekday, "Hour": hour, "Minute": minute})
    return weekday_entries


def main() -> None:
    args = parse_args()
    launch_agents_dir = Path.home() / "Library" / "LaunchAgents"
    launch_agents_dir.mkdir(parents=True, exist_ok=True)

    plist_path = launch_agents_dir / f"{LABEL}.plist"
    log_dir = args.project_dir / "results" / "reversal_3_0_live"
    log_dir.mkdir(parents=True, exist_ok=True)

    plist_data = {
        "Label": LABEL,
        "ProgramArguments": [
            args.python_bin,
            str((args.project_dir / "reversal_3_0_live.py").resolve()),
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
    print("06:30, 07:30, 08:30, 09:30, 10:30, 11:30, 12:00, 12:30 on weekdays")


if __name__ == "__main__":
    main()
