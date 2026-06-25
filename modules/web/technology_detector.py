import requests

from core.logger import write_log
from core.report import save_report


class TechnologyDetector:

    def detect(self, target: str):

        if not target.startswith(
            ("http://", "https://")
        ):
            target = "https://" + target

        write_log(
            f"Technology Detection -> {target}"
        )

        response = requests.get(
            target,
            timeout=10
        )

        html = response.text.lower()

        headers = response.headers

        technologies = []

        server = headers.get(
            "Server",
            ""
        )

        powered = headers.get(
            "X-Powered-By",
            ""
        )

        if "cloudflare" in server.lower():
            technologies.append(
                "Cloudflare"
            )

        if "nginx" in server.lower():
            technologies.append(
                "Nginx"
            )

        if "apache" in server.lower():
            technologies.append(
                "Apache"
            )

        if "php" in powered.lower():
            technologies.append(
                "PHP"
            )

        if "wordpress" in html:
            technologies.append(
                "WordPress"
            )

        if "wp-content" in html:
            technologies.append(
                "WordPress"
            )

        if "laravel" in html:
            technologies.append(
                "Laravel"
            )

        if "__next" in html:
            technologies.append(
                "Next.js"
            )

        if "react" in html:
            technologies.append(
                "React"
            )

        if "vue" in html:
            technologies.append(
                "Vue.js"
            )

        if "django" in html:
            technologies.append(
                "Django"
            )

        result = {

            "target": target,

            "server": server,

            "powered_by": powered,

            "technologies":
                list(
                    set(
                        technologies
                    )
                )
        }

        save_report(
            "technology",
            result
        )

        return result