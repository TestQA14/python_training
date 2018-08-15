# -*- coding: utf-8 -*-
from model.project import Project
from random import randrange


def test_delete_first_project(app):
    app.project.check_count_projects()
    old_projects = app.project.get_project_list()
    app.project.delete_first_project()
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[0:1] = []
    assert old_projects == new_projects


def test_delete_some_project(app):
    app.project.check_count_projects()
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index+1] = []
    assert old_projects == new_projects


#def test_exit_project(app):
#    app.project.check_count_projects()
#    old_projects = app.project.get_project_list()
#    app.project.exit_from_project()
#    new_projects = app.project.get_project_list()
#    old_projects[0:1] = []

