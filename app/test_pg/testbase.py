import yaml
from app.pgobject.app import App


class Testbase:
    def setup(self):
        self.app = App()

    def yaml(self, file_name):
        with open(file_name, encoding='utf-8') as f:
            return yaml.safe_load(f)