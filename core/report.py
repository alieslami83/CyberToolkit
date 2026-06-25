import json

from pathlib import Path
from datetime import datetime

REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)


def save_report(name: str, data: dict):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        REPORT_DIR /
        f"{name}_{timestamp}.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    return filename