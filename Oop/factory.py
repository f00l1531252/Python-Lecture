import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year -((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age)

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year -((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)

class Baby(Person):
    pass


luffy = Person('Luffy', 19)
aki = Person.create_from_dob('aki', 1991, 1, 4)
luka = Person.create_from_dob2('luka', 1999, 1, 29)

mit = Baby.create_from_dob('mit', 2001, 1, 29)
fuka = Baby.create_from_dob2('fuka', 1989, 5, 29)

print(luffy.age)
print(aki.age)
print(type(luffy))

print(type(aki))
print(type(luka))

print(type(mit))
print(type(fuka))
