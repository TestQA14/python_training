
class ProjectHelper:

    def __init__(self, app):
        self.app = app

     # methods
    def create_project(self, project_name, project_description):
            wd = self.app.wd
            self.app.open_projects_page()
            self.click_on_create_button()
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
            self.app.open_projects_page()
            self.app.open_edit_project_page()
            wd.find_element_by_id("project_name").click()
            wd.find_element_by_id("project_name").clear()
            wd.find_element_by_id("project_name").send_keys(project_name)
            wd.find_element_by_id("project_description").click()
            wd.find_element_by_id("project_description").clear()
            wd.find_element_by_id("project_description").send_keys(project_description)
            wd.find_element_by_xpath("//*[@id='form_add_project']/div[6]/input").click()

    def exit_from_project(self):
            wd = self.wd
            self.app.open_projects_page()
            wd.find_element_by_xpath("//div[@class='prj'][1]/span/input[@type='checkbox']").click()
            wd.find_element_by_xpath("//*[@id='span_delete_button']/div").click()
            wd.find_element_by_id("popup_ok").click()

    def delete_project(self):
            wd = self.wd
            self.app.open_edit_project_page()
            wd.find_element_by_xpath("//*[@id='main']/div/div/span").click()
            wd.find_element_by_id("popup_ok").click()

    def create_build(self, build_name, build_created_date):
            wd = self.wd
            self.app.open_builds_of_project_page()
            self.click_on_create_button()
            wd.find_element_by_id("build_created_at").click()
            wd.find_element_by_id("build_created_at").clear()
            wd.find_element_by_id("build_created_at").send_keys(build_created_date)
            wd.find_element_by_id("build_name").click()
            wd.find_element_by_id("build_name").clear()
            wd.find_element_by_id("build_name").send_keys(build_name)
            wd.find_element_by_xpath("//*[@id ='build_form']/div[3]/button").click()

    def click_on_create_button(self):
            wd = self.wd
            wd.find_element_by_xpath("//*[@id='controlmenu']/span[1]").click()

    def click_on_edit_button(self):
            wd = self.wd
            wd.find_element_by_xpath("//*[@id='controlmenu']/span[2]").click()

    def click_on_delete_button(self):
            wd = self.wd
            wd.find_element_by_xpath("//*[@id='controlmenu']/span[3]").click()

    def edit_build(self):
            wd = self.wd
            self.app.open_builds_of_project_page()
            wd.find_element_by_xpath("//div[@class='prj'][1]/span/input[@type='checkbox']").click()
