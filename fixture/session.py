
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email="chemisova.irina2012@gmail.com", password="test123456"):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("user_auth_email").click()
        wd.find_element_by_id("user_auth_email").clear()
        wd.find_element_by_id("user_auth_email").send_keys(email)
        wd.find_element_by_id("user_auth_password").click()
        wd.find_element_by_id("user_auth_password").clear()
        wd.find_element_by_id("user_auth_password").send_keys(password)
        wd.find_element_by_xpath("/html/body/div/fieldset/div[2]/form/div/input").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[@id='quit']").click()
