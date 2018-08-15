from sys import maxsize


class UsersInProject:
    def __init__(self, name=None, email=None, role=None): #id = None):
        self.name = name
        self.email = email
        self.role = role
 #       self.id = id

    def __repr__(self):
        return "%s:%s" (self.email, self.role)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.email == other.email and self.role == other.role

    def id_or_max(self):
        if self.id:
            return self.id
        else:
            return maxsize