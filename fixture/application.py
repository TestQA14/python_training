from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.navigation import PageHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.user import UsersHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.user = UsersHelper(self)
        self.project = ProjectHelper(self)
        self.page = PageHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://chlist.sitechco.ru/")

    def open_projects_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/project") and len(wd.find_elements_by_xpath('//*[@id="controlmenu"]/span[1]/div')) > 0:
            wd.get("https://chlist.sitechco.ru/project")

    def open_edit_project_page(self):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="span_edit_button"]/div').click()

    def select_first(self, wd):
        wd.find_element_by_xpath('//div[@class="prj"][1]/span/input[@type="checkbox"]').click()

    def open_builds_of_project_page(self):
        wd = self.wd
        self.open_projects_page()
        self.select_first(wd)
        wd.find_element_by_xpath('//*[@id="span_edit_button"]/div').click()
        wd.find_element_by_xpath('//*[@id="main"]/div/div/a[1]').click()

    def is_valid(self):
        try:
           c_url = str(self.wd.current_url)
           if not c_url == "data:,":
                return True
        except:
            return False

    def destroy(self):
            self.wd.quit()
