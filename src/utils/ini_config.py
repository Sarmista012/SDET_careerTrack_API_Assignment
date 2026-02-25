from configparser import ConfigParser
from pathlib import Path

class IniConfig:
    def __init__(self, ini_path: str):
        p = Path(ini_path).resolve()
        if not p.exists():
            raise FileNotFoundError(f"INI not found: {p}")

        self.path = p
        self._parser = ConfigParser()


        with p.open("r", encoding="utf-8-sig") as f:
            self._parser.read_file(f)

    def get(self, section: str, key: str) -> str:
        return self._parser.get(section, key).strip()
