import socket
import requests

from core.logger import write_log
from core.report import save_report


class IPInfo:

    def __init__(self, timeout=10):

        self.timeout = timeout

    def resolve_target(self, target):

        try:
            return socket.gethostbyname(target)

        except socket.gaierror:

            raise ValueError(
                f"Cannot resolve {target}"
            )

    def lookup(self, target):

        ip = self.resolve_target(target)

        providers = [

            f"https://ipwho.is/{ip}",
            f"https://ipapi.co/{ip}/json/"
        ]

        for url in providers:

            try:

                response = requests.get(
                    url,
                    timeout=self.timeout
                )

                data = response.json()

                if data:

                    write_log(
                        f"IP Lookup Success -> {ip}"
                    )

                    save_report(
                        "ip_info",
                        data
                    )

                    return data

            except Exception:
                continue

        raise RuntimeError(
            "All providers failed"
        )