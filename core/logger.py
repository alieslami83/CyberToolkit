from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)


def write_log(message: str):

    logfile = LOG_DIR / (
        f"{datetime.now().strftime('%Y-%m-%d')}.log"
    )

    with open(
        logfile,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"{message}\n"
        )