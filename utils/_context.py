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
    project_root: str = field(default_factory=lambda: str(Path(__file__).resolve().parents[1]), init=False, repr=False)

    def set_context(self, env, log_level):
        self.env = env
        self.log_level = log_level
        config_file = f"{self.project_root}/config/{self.env}.yaml"
        with open(config_file) as f:
            conf = yaml.safe_load(f.read())

            self.url = conf["url"]
            self.username = conf["username"]
            self.password = conf["password"]
            self.api_host=conf["host"]

ctx = Context()