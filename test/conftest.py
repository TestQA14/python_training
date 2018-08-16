# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseURL")
        fixture = Application(browser=browser, base_url=base_url)
        fixture.session.login(email="chemisova.irina2012@gmail.com", password="test123456")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.ensure_login(email="chemisova.irina2012@gmail.com", password="test123456")
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
    parser.addoption("--baseURL", action="store", default="https://chlist.sitechco.ru/")
