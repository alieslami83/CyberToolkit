from pathlib import Path
from datetime import datetime


class Statistics:

    def get_stats(self):

        reports_dir = Path("reports")
        logs_dir = Path("logs")

        reports = list(
            reports_dir.glob("*")
        )

        logs = list(
            logs_dir.glob("*")
        )

        latest_report = "N/A"

        if reports:

            latest = max(
                reports,
                key=lambda x: x.stat().st_mtime
            )

            latest_report = latest.name

        total_size = 0

        for report in reports:

            total_size += report.stat().st_size

        return {

            "version": "0.3.0",

            "reports_count":
                len(reports),

            "logs_count":
                len(logs),

            "latest_report":
                latest_report,

            "reports_size_kb":
                round(
                    total_size / 1024,
                    2
                )
        }