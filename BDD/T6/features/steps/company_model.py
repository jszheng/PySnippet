# file:features/steps/company_model.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
class Department(object):
    def __init__(self, name, members=None):
        if not members:
            members = []
        self.name = name
        self.members = members

    def add_member(self, name):
        assert name not in self.members
        self.members.append(name)

    @property
    def count(self):
        return len(self.members)

    def __len__(self):
        return self.count

class CompanyModel(object):
    def __init__(self):
        self.users = []
        self.departments = {}

    def add_user(self, name, deparment):
        assert name not in self.users
        if not deparment in self.departments:
            self.departments[deparment] = Department(deparment)
        self.departments[deparment].add_member(name)

    def count_persons_per_department(self):
        pass

    def get_headcount_for(self, department):
        return self.departments[department].count

