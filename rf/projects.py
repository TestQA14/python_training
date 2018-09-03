from fixture.application import Application
import os.path
import json
from model.project import Project
class Projects:

    def __init__(self, browser='chrome', config='target.json'):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseURL'])
        pass

    def destroy_fixtures(self):
        self.fixture.destroy()

    def create_project(self, name, description):
        self.fixture.project.create(Project(name=name, description=description))
