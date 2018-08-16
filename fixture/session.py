
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("user_auth_email").click()
        wd.find_element_by_id("user_auth_email").clear()
        wd.find_element_by_id("user_auth_email").send_keys(email)
        wd.find_element_by_id("user_auth_password").click()
        wd.find_element_by_id("user_auth_password").clear()
        wd.find_element_by_id("user_auth_password").send_keys(password)
        wd.find_element_by_xpath("/html/body/div/fieldset/div[2]/form/div/input").click()
        wd.refresh()

    def logout(self):
        wd = self.app.wd
        wd.get("https://chlist.sitechco.ru/logout")
       # wd.find_element_by_id("quit").click()
        wd.refresh()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        if wd.find_element_by_id("username").isDisplayed():
            return len(wd.find_element_by_id("username")).text == "test"
        else:
            return False

    def ensure_login(self, email, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(email):
                return
            else:
                self.logout()
        self.login(email, password)

    def is_logged_in_as(self, email):
        wd = self.app.wd
        wd.find_element_by_id("username").click()
        return self.get_logged_user() == email

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_id("user_email").text[1:-1]
