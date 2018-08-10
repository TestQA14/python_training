from selenium.webdriver.chrome.webdriver import WebDriver
class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

        # methods
    def create_project(self, project_name, project_description):
            wd = self.wd
            self.open_projects_page()
            wd.find_element_by_xpath("//*[@id='controlmenu']/span[1]").click()
            wd.find_element_by_id("project_name").click()
            wd.find_element_by_id("project_name").clear()
            wd.find_element_by_id("project_name").send_keys(project_name)
            wd.find_element_by_id("project_description").click()
            wd.find_element_by_id("project_description").clear()
            wd.find_element_by_id("project_description").send_keys(project_description)
            wd.find_element_by_id("project_date_type").click()
            wd.find_element_by_xpath("//*[@id='project_date_type']/option[2]").click()
            wd.find_element_by_xpath("//*[@id='form_add_project']/div[6]/input").click()

    def edit_project(self, project_name, project_description):
            wd = self.wd
            self.open_projects_page()
            wd.find_element_by_xpath("//div[@class='prj'][1]/span/input[@type='checkbox']").click()
            wd.find_element_by_xpath("//*[@id='span_edit_button']/div").click()
            wd.find_element_by_id("project_name").click()
            wd.find_element_by_id("project_name").clear()
            wd.find_element_by_id("project_name").send_keys(project_name)
            wd.find_element_by_id("project_description").click()
            wd.find_element_by_id("project_description").clear()
            wd.find_element_by_id("project_description").send_keys(project_description)
            wd.find_element_by_xpath("//*[@Id='form_add_project']/div[6]/input").click()

    def delete_project(self):
            wd = self.wd
            self.open_projects_page()
            wd.find_element_by_xpath("//div[@class='prj'][1]/span/input[@type='checkbox']").click()
            wd.find_element_by_id("span_delete_button").click()
            wd.find_element_by_id("popup_ok").click()

    def sign_up(self, users):
            wd = self.wd
            self.open_home_page()
            wd.find_element_by_xpath("/html/body/div/fieldset/div[2]/form/div/a[1]").click()
            wd.find_element_by_id("user_name").click()
            wd.find_element_by_id("user_name").clear()
            wd.find_element_by_id("user_name").send_keys(users.firstname)
            # email
            wd.find_element_by_id("user_email").click()
            wd.find_element_by_id("user_email").clear()
            wd.find_element_by_id("user_email").send_keys(users.email)
            # passw
            wd.find_element_by_id("user_password").click()
            wd.find_element_by_id("user_password").clear()
            wd.find_element_by_id("user_password").send_keys(users.password)
            # checkbox
            wd.find_element_by_id("user_password").click()
            # press button signup
            wd.find_element_by_id("user_is_subscribed").click()
            wd.find_element_by_id("user_notification").click()
            wd.find_element_by_id("user_is_polit").click()  # agree
            wd.find_element_by_id("submit_button").click()

    def login(self, email="chemisova.irina2012@gmail.com", password="test123456"):
            wd = self.wd
            self.open_home_page()
            wd.find_element_by_id("user_auth_email").click()
            wd.find_element_by_id("user_auth_email").clear()
            wd.find_element_by_id("user_auth_email").send_keys(email)
            wd.find_element_by_id("user_auth_password").click()
            wd.find_element_by_id("user_auth_password").clear()
            wd.find_element_by_id("user_auth_password").send_keys(password)
            wd.find_element_by_xpath("/html/body/div/fieldset/div[2]/form/div/input").click()

    def open_home_page(self):
            wd = self.wd
            wd.get("https://chlist.sitechco.ru/")

    def open_projects_page(self):
            wd = self.wd
            wd.get("https://chlist.sitechco.ru/project")

    def destroy(self):
        self.wd.quit()
