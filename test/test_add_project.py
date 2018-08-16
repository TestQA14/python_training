# -*- coding: utf-8 -*-

from model.project import Project
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name="new_project_1", description="description_project_1"),
            Project(name="new_project_2", description=""),
            Project(name="new_project_3", description="description_project_3")]

testdata1 = [Project(name=random_string("name", 10), description=random_string("description", 40))
             for i in range(5)]


testdata2 = [Project(name="", description="")] + [
             Project(name=random_string("name", 10), description=random_string("description", 40))
             for i in range(5)]

testdata3 = [
             Project(name=name, description=description)
             for name in ["", random_string("name", 10)]
             for description in ["", random_string("description", 30)]]

testdata4 = [Project(name=random_string("", 20), description=random_string("", 60))
             for i in range(5)]


def test_create_project(app):
    for project in testdata4:
        old_projects = app.project.get_project_list()
        app.project.create(project)
        assert len(old_projects) + 1 == app.project.count()
        new_projects = app.project.get_project_list()
        old_projects.append(project)
        old_projects = app.project.get_project_list()
        assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


@pytest.mark.parametrize("project", testdata2, ids=[repr(x) for x in testdata2])
def test_add_new_projects(app, project):
    pass

def test_create_build(app):
    app.project.create_build(build_name="test_build", build_created_date="10.08.2018")


def test_load_list_project(app):
    app.open_projects_page()
    old_projects = app.project.get_project_list()
    app.project.create(Project(name="new_project_1", description="description_project_1"))
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
# checklist

