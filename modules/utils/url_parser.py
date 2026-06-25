from urllib.parse import urlparse, parse_qs

from core.logger import write_log
from core.report import save_report


class URLParser:

    def parse(self, url: str):

        parsed = urlparse(url)

        result = {
            "scheme": parsed.scheme,
            "hostname": parsed.hostname,
            "port": parsed.port,
            "path": parsed.path,
            "query": parsed.query,
            "parameters": parse_qs(
                parsed.query
            )
        }

        write_log(
            f"URL Parsed -> {url}"
        )

        save_report(
            "url_parser",
            result
        )

        return result