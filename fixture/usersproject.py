# -*- coding: utf-8 -*-
from model.users_in_project import UsersInProject
import re


class UsersProjectHelper:

    def __init__(self,app):
        self.app = app

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    users_project_cache = None

    def get_users_list(self):
        if self.users_project_cache is None:
            wd = self.app.wd
            self.app.open_projects_page()
            self.app.select_first_project()
            self.app.click_on_edit_button()
            wd.find_element_by_xpath('//*[@id="main"]/div/div/a[4]').click()
            self.users_project_cache = []
            for row in wd.find_elements_by_xpath('//div[@class="prj"]'):
                cells = row.find_elements_by_tag_name("span")
                first_line = cells[1].text.split()
                email = cells[3].text
                role = cells[2].text
                self.users_project_cache.append(UsersInProject(name=first_line[1], email=email, role=role))# id=id,
        return list(self.users_project_cache)

    def open_user_project_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_projects_page()
        self.app.select_first_project()
        self.app.click_on_edit_button()
        wd.find_element_by_xpath('//*[@id="main"]/div/div/a[4]').click()
        row = wd.find_elements_by_xpath('//div[@class="prj"]')[index].click()
        self.app.click_on_edit_button()

    def open_users_project_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_projects_page()
        self.app.select_first_project()
        self.app.click_on_edit_button()
        wd.find_element_by_xpath('//*[@id="main"]/div/div/a[4]').click()
        row = wd.find_elements_by_xpath('//div[@class="prj"]')[index]
        cells = row.find_elements_by_tag_name("span")[1]
        cells.find_element_by_tag_name("a").click()



    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_project_to_edit_by_index(index)
        name = wd.find_element_by_name("user[name]").get_attribute("value")
        email = wd.find_element_by_name("user[email]").get_attribute("value")
        role = wd.find_element_by_xpath('//*[@id="user_role_id"]/option[@selected]').text
        return UsersInProject(name=name, email=email, role=role)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_users_project_view_by_index(index)
        text = wd.find_element_by_xpath('//*[@id="main"]/div/div[2]').text
        name = re.search(u"ИМЯ: (.*)", text).group(1)
        email = re.search("EMAIL: (.*)", text).group(1)
        role = re.search(u"РОЛЬ: (.*)", text).group(1)
        return UsersInProject(name=name, email=email, role=role)

    def clear(s):
        return re.sub("[() -]", "", s)