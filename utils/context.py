from dataclasses import dataclass, field
from pathlib import Path
import yaml
from utils.singleton import singleton


@singleton
@dataclass
class Context:
    env: str = field(default="")
    log_level: str = field(default="INFO")
    url: str = field(default="", init=False, repr=False)
    username: str = field(default="", init=False, repr=False)
    password: str = field(default="", init=False, repr=False)
    api_host: str = field(default="", init=False, repr=False)
    project_root: str = field(default="", init=False, repr=False)

    def __post_init__(self):
        if not self.env:
            raise ValueError("Env cannot be blank")

        self._set_context()

    def _set_context(self):

        project_root = Path(__file__).resolve().parents[1]
        config_file = project_root / "config" / f"{self.env}.yaml"

        with config_file.open() as f:
            conf = yaml.safe_load(f.read())

            self.url = conf["url"]
            self.username = conf["username"]
            self.password = conf["password"]
            self.api_host=conf["host"]
            self.project_root = self.project_root = str(Path(__file__).resolve().parents[2])

