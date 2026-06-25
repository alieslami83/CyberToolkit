from pathlib import Path


class Dashboard:

    def get_stats(self):

        reports = len(
            list(
                Path("reports").glob("*.json")
            )
        )

        logs = len(
            list(
                Path("logs").glob("*.log")
            )
        )

        modules = 14

        return {
            "version": "0.3.0",
            "reports": reports,
            "logs": logs,
            "modules": modules
        }