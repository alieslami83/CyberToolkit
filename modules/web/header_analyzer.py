import requests

from core.logger import write_log
from core.report import save_report


class HeaderAnalyzer:

    SECURITY_HEADERS = [

        "Content-Security-Policy",

        "Strict-Transport-Security",

        "X-Frame-Options",

        "X-Content-Type-Options",

        "Referrer-Policy",

        "Permissions-Policy"
    ]

    def analyze(self, url: str):

        if not url.startswith(
            ("http://", "https://")
        ):
            url = "https://" + url

        write_log(
            f"Header Analysis Started -> {url}"
        )

        response = requests.get(
            url,
            timeout=10
        )

        headers = dict(
            response.headers
        )

        security = {}

        for header in self.SECURITY_HEADERS:

            security[header] = (
                "Present"
                if header in headers
                else "Missing"
            )

        result = {

            "status_code":
                response.status_code,

            "server":
                headers.get("Server"),

            "content_type":
                headers.get("Content-Type"),

            "security_headers":
                security
        }

        save_report(
            "headers",
            result
        )

        return result