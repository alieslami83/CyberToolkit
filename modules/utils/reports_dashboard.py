from pathlib import Path
from datetime import datetime


class ReportsDashboard:

    REPORT_DIR = Path("reports")

    def get_reports(self):

        if not self.REPORT_DIR.exists():
            return []

        reports = []

        for file in self.REPORT_DIR.glob("*.json"):

            reports.append({
                "name": file.name,
                "size_kb": round(
                    file.stat().st_size / 1024,
                    2
                ),
                "modified": datetime.fromtimestamp(
                    file.stat().st_mtime
                ).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

        return sorted(
            reports,
            key=lambda x: x["modified"],
            reverse=True
        )