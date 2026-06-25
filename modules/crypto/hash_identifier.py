import re

from core.logger import write_log
from core.report import save_report


class HashIdentifier:

    def identify(self, hash_value: str):

        hash_value = hash_value.strip()

        patterns = {
            "MD5": r"^[a-fA-F0-9]{32}$",
            "SHA1": r"^[a-fA-F0-9]{40}$",
            "SHA224": r"^[a-fA-F0-9]{56}$",
            "SHA256": r"^[a-fA-F0-9]{64}$",
            "SHA384": r"^[a-fA-F0-9]{96}$",
            "SHA512": r"^[a-fA-F0-9]{128}$"
        }

        matches = []

        for algorithm, pattern in patterns.items():

            if re.fullmatch(
                pattern,
                hash_value
            ):
                matches.append(
                    algorithm
                )

        result = {
            "hash": hash_value,
            "possible_algorithms": matches
        }

        write_log(
            "Hash Identification Performed"
        )

        save_report(
            "hash_identifier",
            result
        )

        return result