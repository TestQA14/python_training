from model.project import Project
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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

testdata3 = [Project(name=name, description=description)
             for name in ["", random_string("name", 10)]
             for description in ["", random_string("description", 30)]]

testdata4 = [Project(name=random_string("", 20), description=random_string("", 60))
             for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)  #"../data/projects.json")

with open(file, "w") as opened_file:
    opened_file.write(json.dumps(testdata, default=lambda x:   x.__dict__, indent=2))
