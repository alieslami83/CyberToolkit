import json
from pathlib import Path


class HTMLReportGenerator:

    def generate(self, json_file: str):

        json_path = Path(json_file)

        if not json_path.exists():
            raise FileNotFoundError(
                "Report not found"
            )

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        html = """
        <html>
        <head>
            <title>CyberToolkit Report</title>
            <style>
                body{
                    font-family:Arial;
                    margin:40px;
                }

                table{
                    border-collapse:collapse;
                    width:100%;
                }

                td,th{
                    border:1px solid #ccc;
                    padding:8px;
                }

                th{
                    background:#eee;
                }
            </style>
        </head>
        <body>

        <h1>CyberToolkit Report</h1>

        <table>

        <tr>
            <th>Field</th>
            <th>Value</th>
        </tr>
        """

        for key, value in data.items():

            html += f"""
            <tr>
                <td>{key}</td>
                <td>{value}</td>
            </tr>
            """

        html += """
        </table>

        </body>
        </html>
        """

        output = json_path.with_suffix(
            ".html"
        )

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

        return str(output)