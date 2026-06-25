import json
import base64

from core.logger import write_log
from core.report import save_report


class JWTDecoder:

    def _decode_part(
        self,
        data: str
    ):

        padding = (
            4 - len(data) % 4
        ) % 4

        data += "=" * padding

        decoded = base64.urlsafe_b64decode(
            data
        )

        return json.loads(
            decoded.decode()
        )

    def decode(
        self,
        token: str
    ):

        parts = token.split(
            "."
        )

        if len(parts) != 3:

            raise ValueError(
                "Invalid JWT"
            )

        header = self._decode_part(
            parts[0]
        )

        payload = self._decode_part(
            parts[1]
        )

        result = {

            "header": header,

            "payload": payload
        }

        write_log(
            "JWT Decoded"
        )

        save_report(
            "jwt_decoder",
            result
        )

        return result