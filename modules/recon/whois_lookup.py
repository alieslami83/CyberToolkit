import whois

from core.logger import write_log
from core.report import save_report


class WhoisLookup:

    def lookup(self, domain: str):

        write_log(
            f"WHOIS Lookup Started -> {domain}"
        )

        data = whois.whois(domain)

        result = {
            "domain": str(data.domain_name),
            "registrar": str(data.registrar),
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "updated_date": str(data.updated_date),
            "name_servers": data.name_servers,
            "status": data.status,
            "emails": data.emails
        }

        save_report(
            f"whois_{domain}",
            result
        )

        write_log(
            f"WHOIS Lookup Finished -> {domain}"
        )

        return result