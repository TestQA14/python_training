# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
import json
import os.path
import importlib

fixture = None
target = None
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as opened_file:
            target = json.load(opened_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        fixture.session.login(email=target['admin_email'], password=target['admin_password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
#    parser.addoption("--baseURL", action="store", default="https://chlist.sitechco.ru/")
#    parser.addoption("--adminPassword", action="store", default="")
#    parser.addoption("--adminEmail", action="store", default="")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            constant = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, constant, ids=[str(x) for x in constant])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).constant
