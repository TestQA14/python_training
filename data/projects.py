from model.project import Project
import random
import string


constant = [
    Project(name="name1", description="description1"), Project(name="name2", description="description2"),
    Project(name="name3", description="description3"), Project(name="name4", description="description4"),
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata0 = [Project(name="new_project_1", description="description_project_1"),
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
