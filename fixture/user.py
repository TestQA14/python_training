
class UsersHelper:

    def __init__(self, app):
        self.app = app

    def sign_up(self, users):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("/html/body/div/fieldset/div[2]/form/div/a[1]").click()
        wd.find_element_by_id("user_name").click()
        wd.find_element_by_id("user_name").clear()
        wd.find_element_by_id("user_name").send_keys(users.firstname)
        wd.find_element_by_id("user_email").click()
        wd.find_element_by_id("user_email").clear()
        wd.find_element_by_id("user_email").send_keys(users.email)
        wd.find_element_by_id("user_password").click()
        wd.find_element_by_id("user_password").clear()
        wd.find_element_by_id("user_password").send_keys(users.password)
        wd.find_element_by_id("user_password").click()
        wd.find_element_by_id("user_is_subscribed").click()
        wd.find_element_by_id("user_notification").click()
        wd.find_element_by_id("user_is_polit").click()  # agree
        wd.find_element_by_id("submit_button").click()