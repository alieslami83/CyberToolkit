import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

from core.logger import write_log
from core.report import save_report


class PortScanner:

    def __init__(self, timeout=1, threads=100):
        self.timeout = timeout
        self.threads = threads

    def scan_port(self, host: str, port: int):

        try:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(
                self.timeout
            )

            result = sock.connect_ex(
                (host, port)
            )

            sock.close()

            return port if result == 0 else None

        except Exception:
            return None

    def scan(
        self,
        host: str,
        ports: list[int]
    ):

        write_log(
            f"Port Scan Started -> {host}"
        )

        open_ports = []

        with ThreadPoolExecutor(
            max_workers=self.threads
        ) as executor:

            futures = [

                executor.submit(
                    self.scan_port,
                    host,
                    port
                )

                for port in ports
            ]

            for future in as_completed(
                futures
            ):

                result = future.result()

                if result:
                    open_ports.append(
                        result
                    )

        result_data = {
            "host": host,
            "open_ports": sorted(
                open_ports
            )
        }

        save_report(
            f"portscan_{host}",
            result_data
        )

        write_log(
            f"Port Scan Finished -> {host}"
        )

        return result_data