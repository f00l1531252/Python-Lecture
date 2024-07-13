class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print('get_age called')
        return self._age

    @age.setter
    def age(self, age):
        print('set_age called')
        if age < 0:
            print('０以上の値を入力してください')
        else:
            self._age = age

    # age = property(get_age, set_age)


luffy = Person('Luffy', 19)
print(luffy.age)
luffy.age = -10
