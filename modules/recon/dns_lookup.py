import dns.resolver

from core.logger import write_log
from core.report import save_report


class DNSLookup:

    RECORD_TYPES = [

        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME"
    ]

    def lookup(self, domain):

        results = {}

        write_log(
            f"DNS Lookup Started -> {domain}"
        )

        for record in self.RECORD_TYPES:

            try:

                answers = dns.resolver.resolve(
                    domain,
                    record
                )

                results[record] = [

                    str(answer)

                    for answer in answers
                ]

            except Exception:

                results[record] = []

        save_report(
            f"dns_{domain}",
            results
        )

        return results