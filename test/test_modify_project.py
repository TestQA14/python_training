# -*- coding: utf-8 -*-
from random import randrange

from model.project import Project


def test_edit_first_project(app):
    app.project.check_count_projects()
    old_projects = app.project.get_project_list()
    project_1 = Project(name="Test test test")
    index = randrange(len(old_projects))
    project_1.id = old_projects[index].id
    app.project.edit_some_project(index, project_1)
    new_projects = app.project.get_project_list()
    assert len(old_projects) == len(new_projects)


def test_edit_some_project(app):
    app.project.check_count_projects()
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    project_1 = Project(name="New project1")
    project_1.id = old_projects[index].id
    app.project.edit_some_project(index, project_1)
    new_projects = app.project.get_project_list()
    assert len(old_projects) == len(new_projects)
#    old_projects[index] = project_1
#    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

#def test_edit_name_of_first_project(app):
#    app.project.check_count_projects()
#    old_projects = app.project.get_project_list()
#    app.project.edit_first_project(Project(name="test_project_3"))
#    new_projects = app.project.get_project_list()
#    assert len(old_projects) == len(new_projects)


# def test_edit_description_of_first_project(app):
#    app.project.check_count_projects()
#    old_projects = app.project.get_project_list()
#    app.project.edit_first_project(Project(description="test project 3 description text"))
#    new_projects = app.project.get_project_list()
#    assert len(old_projects) == len(new_projects)


#def test_clear_description_of_first_project(app):
#    app.project.check_count_projects()
#    old_projects = app.project.get_project_list()
#    app.project.edit_first_project(Project(description=""))
#    new_projects = app.project.get_project_list()
#    assert len(old_projects) == len(new_projects)

