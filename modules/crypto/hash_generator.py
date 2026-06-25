import hashlib

from core.logger import write_log
from core.report import save_report


class HashGenerator:

    def generate(self, text: str):

        result = {

            "md5":
                hashlib.md5(
                    text.encode()
                ).hexdigest(),

            "sha1":
                hashlib.sha1(
                    text.encode()
                ).hexdigest(),

            "sha256":
                hashlib.sha256(
                    text.encode()
                ).hexdigest(),

            "sha512":
                hashlib.sha512(
                    text.encode()
                ).hexdigest()
        }

        write_log(
            "Hash Generated"
        )

        save_report(
            "hash",
            result
        )

        return result