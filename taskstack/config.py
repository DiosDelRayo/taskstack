from typing import Optional, Union
from yaml import safe_load as load
from os.path import expanduser

class Config:

    instance: 'Config' = None

    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.config = load(f.read())
            f.close()

    def github_token(self) -> Optional[str]:

        if 'github' not in self.config or 'token' not in self.config.get('github'):
            return None
        return self.config.get('github').get('token')

    def repository(self, default: Union[None, str] = None) -> Optional[str]:
        if 'repository' not in self.config:
            return default
        return self.config.get('repository')


    @classmethod
    def get(cls) -> 'Config':
        if cls.instance is None:
            cls.instance = Config(expanduser('~/.config/taskstack/config.yml'))
        return cls.instance
