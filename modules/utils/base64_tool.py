import base64

from core.logger import write_log
from core.report import save_report


class Base64Tool:

    def encode(self, text: str):

        result = base64.b64encode(
            text.encode()
        ).decode()

        write_log(
            "Base64 Encode"
        )

        save_report(
            "base64_encode",
            {
                "input": text,
                "output": result
            }
        )

        return result

    def decode(self, text: str):

        try:

            result = base64.b64decode(
                text
            ).decode()

            write_log(
                "Base64 Decode"
            )

            save_report(
                "base64_decode",
                {
                    "input": text,
                    "output": result
                }
            )

            return result

        except Exception:

            return "Invalid Base64"