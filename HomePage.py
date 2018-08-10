# -*- coding: utf-8 -*-
import pytest
from users import User
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# login / signup


def test_login(app):
    app.login(email="chemisova.irina2012@gmail.com", password="test123456")


def test_empty_login(app):
    app.login(email="", password="")


def test_signup(app):
    app.sign_up(User(firstname="Firstname123", email="testemai321l@gmail.com", password="pas123s"))


def test_empty_signup(app):
    app.sign_up(User(firstname="", email="", password=""))

# project


def test_create_project(app):
    app.login(email="chemisova.irina2012@gmail.com", password="test123456")
    app.create_project("project_1", "description_project_1")


def test_delete_project(app):
    app.login(email="chemisova.irina2012@gmail.com", password="test123456")
    app.delete_project()


def test_exit_project(app):
    app.login(email="chemisova.irina2012@gmail.com", password="test123456")
    app.exit_from_project()


def test_edit_project(app):
    app.login(email="chemisova.irina2012@gmail.com", password="test123456")
    app.edit_project("test_project_1", "new_description_project_1")

# checklist

