__author__ = 'jszheng'


class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3]

        def __set__(self, instance, value):
            value = value.replace('-', '')
            print(instance)
            print(instance.acctlen)
            print(instance.__dict__)
            print(dir(instance))
            print(type(instance))
            print(type(instance.acctlen))
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                self.acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError('cannot set remain')
    remain = Remain()

if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr)
    try:
        bob.age = 200
    except:
        print('Bad Age')

    try:
        bob.remain = 5
    except:
        print('Can\'t set remain')

    try:
        bob.acct = '1234567'
    except:
        print('Wrong Size of Acct')

    print(bob.__dict__)
    print(id(bob.acctlen))

    sue = CardHolder('1234-5678', 'Sue Smith', 40, '123 main st')
    print(id(sue.acctlen))

    CardHolder.acctlen = 10
    print(bob.acctlen)
    print(sue.acctlen)

