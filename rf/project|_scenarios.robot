*** Settings ***
Library     rf.projects
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new project
    Create project      name    description
