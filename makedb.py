import person

from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=10000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()

db = shelve.open('persondb')
print("DB length=", len(db))
print(list(db.keys()))
for key in db:
    print(key, '=>', db[key])

