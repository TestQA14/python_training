# -*- coding: utf-8 -*-
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

     # methods
    def create(self, new_project_data):
        wd = self.app.wd
        self.app.open_projects_page()
        self.click_on_create_button()
        self.fill_project_form(new_project_data)
        wd.find_element_by_id("project_date_type").click()
        wd.find_element_by_xpath('//*[@id="project_date_type"]/option[2]').click()
        wd.find_element_by_xpath('//*[@id="form_add_project"]/div[6]/input').click()
        self.app.open_projects_page()
        self.project_cache = None

    def edit_first_project(self):
        self.edit_some_project(0)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_filed_value("project_name", project.name)
        self.change_filed_value("project_description", project.description)

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def exit_from_project(self):
        wd = self.app.wd
        self.app.open_projects_page()
        wd.find_element_by_xpath('//div[@class="prj"][1]/span/input[@type="checkbox"]').click()
        wd.find_element_by_xpath('//*[@id="span_delete_button"]/div').click()
        wd.find_element_by_id("popup_ok").click()
        wd.refresh()
        wd.implicitly_wait(15)

    def delete_first_project(self):
        self.delete_project_by_index(0)

    def create_build(self, build_name, build_created_date):
        wd = self.app.wd
        self.app.open_builds_of_project_page()
        self.click_on_create_button()
        wd.find_element_by_id("build_created_at").click()
        wd.find_element_by_id("build_created_at").clear()
        wd.find_element_by_id("build_created_at").send_keys(build_created_date)
        wd.find_element_by_id("build_name").click()
        wd.find_element_by_id("build_name").clear()
        wd.find_element_by_id("build_name").send_keys(build_name)
        wd.find_element_by_xpath('//*[@id ="build_form"]/div[3]/button').click()

    def click_on_create_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="controlmenu"]/span[1]').click()

    def click_on_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="controlmenu"]/span[2]').click()

    def click_on_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="controlmenu"]/span[3]').click()

    def edit_build(self):
        wd = self.app.wd
        self.app.open_builds_of_project_page()
        wd.find_element_by_xpath('//div[@class="prj"][1]/span/input[@type="checkbox"]').click()
        wd.click_on_edit_button()

    def count(self):
        wd = self.app.wd
        self.app.open_projects_page()
        return len(wd.find_elements_by_css_selector("span.checkbox"))

    def check_count_projects(self):
        wd = self.app.wd
        wd.refresh()
        if self.app.project.count() == 0:
            self.app.project.create(Project(name="test5"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("span.checkbox"):
                 text = element.text
                 element.find_element_by_xpath('//input[@class="my_projects"]').get_attribute("id")
                 self.project_cache.append(Project(name=text, id=id))
        return list(self.project_cache)

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.app.open_projects_page()
        self.select_project_by_index(index)
        self.app.open_edit_project_page()
        wd.find_element_by_xpath('//*[@id="main"]/div/div/span').click()
        wd.find_element_by_id("popup_ok").click()
        self.app.open_projects_page()
        self.project_cache = None

    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//span[@class="checkbox"]')[index].click()

    def edit_some_project(self, index, new_project_data):
        wd = self.app.wd
        self.app.open_projects_page()
        self.select_project_by_index(index)
        self.click_on_edit_button()
        self.fill_project_form(new_project_data)
        wd.find_element_by_xpath('//*[@id="form_add_project"]/div[6]/input').click()
        self.project_cache = None
