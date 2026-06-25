import ssl
import socket
from datetime import datetime

from core.logger import write_log
from core.report import save_report


class SSLAnalyzer:

    def analyze(self, hostname: str):

        write_log(
            f"SSL Analysis Started -> {hostname}"
        )

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443)
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_sock:

                cert = secure_sock.getpeercert()

        result = {

            "subject":
                dict(
                    x[0]
                    for x in cert["subject"]
                ),

            "issuer":
                dict(
                    x[0]
                    for x in cert["issuer"]
                ),

            "version":
                cert["version"],

            "serial_number":
                cert["serialNumber"],

            "not_before":
                cert["notBefore"],

            "not_after":
                cert["notAfter"]
        }

        save_report(
            f"ssl_{hostname}",
            result
        )

        write_log(
            f"SSL Analysis Finished -> {hostname}"
        )

        return result