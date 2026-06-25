import json
from pathlib import Path

from core.logger import write_log


class SettingsManager:

    CONFIG_FILE = Path(
        "config/config.json"
    )

    def load(self):

        with open(
            self.CONFIG_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def save(self, data):

        with open(
            self.CONFIG_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        write_log(
            "Configuration Updated"
        )