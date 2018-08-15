# -*- coding: utf-8 -*-

from model.users import User
from model.project import Project
from sys import maxsize

# login / signup


#def test_login(app):
#   app.session.logout()
#def test_empty_login(app):
#    app.session.login(email="", password="")
#def test_signup(app):
#    app.user.sign_up(User(firstname="Firstname123", email="testemai321l@gmail.com", password="pas123s"))
#def test_empty_signup(app):
#    app.user.sign_up(User(firstname="", email="", password=""))
# project


def test_create_project(app):
    old_projects = app.project.get_project_list()
    project_1 = Project(name="new_project_1", description="description_project_1")
    app.project.create(project_1)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project_1)
    old_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_create_build(app):
    app.project.create_build(build_name="test_build", build_created_date="10.08.2018")


def test_load_list_project(app):
    app.open_projects_page()
    old_projects = app.project.get_project_list()
    app.project.create(Project(name="new_project_1", description="description_project_1"))
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
# checklist

