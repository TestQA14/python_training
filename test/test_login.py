# -*- coding: utf-8 -*-

from model.users import User
from model.project import Project

# login / signup


def test_login(app):
   app.session.logout()


def test_empty_login(app):
   app.session.login(email="", password="")


def test_signup(app):
    app.user.sign_up(User(firstname="Firstname123", email="testemai321l@gmail.com", password="pas123s"))


def test_empty_signup(app):
   app.user.sign_up(User(firstname="", email="", password=""))
