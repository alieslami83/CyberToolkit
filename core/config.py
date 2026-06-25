import json
from pathlib import Path

CONFIG_FILE = Path("config/config.json")


def load_config():

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)