__author__ = 'jszheng'

import collections

Person = collections.namedtuple('Person', 'name age gender', rename=True)
print('Type of Person:', type(Person))

#Bob = Person(name='Bob', gender='male', age=30)
Bob = Person('Bob', 30, 'male')
print('Representation:', Bob)

Jane = Person(name='Jane', age=29, gender='female')
print('Field by name', Jane.name)

Jack = Person._make(['Jack', 40, 'Male'])
Jack = Jack._replace(age=10)
for people in [Bob, Jane, Jack]:
    print("%s is %d years old %s" % people)