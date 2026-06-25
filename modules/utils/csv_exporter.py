import csv
import json
from pathlib import Path


class CSVExporter:

    def export(self, json_file: str):

        json_path = Path(json_file)

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        csv_path = json_path.with_suffix(
            ".csv"
        )

        with open(
            csv_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)

            writer.writerow(
                ["Field", "Value"]
            )

            for key, value in data.items():

                writer.writerow(
                    [key, str(value)]
                )

        return str(csv_path)