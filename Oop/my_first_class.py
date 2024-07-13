class Person:
    num_legs = 2
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f'{self.name} is walking with {Person.num_legs} legs')

    def run(self):
        print(f'{self.name} is running with {Person.num_legs} legs')


luffy = Person('Luffy', 19, 'male')
print(Person.count)
zoro = Person('Zoro', 21, 'male')
print(Person.count)
nami = Person('Nami', 20, 'female')
print(Person.count)


# インスタンス変数　.に続けてアクセス
print(luffy.age)
print(zoro.name)

# インスタンスメソッド
zoro.walk()
luffy.run()

# クラス変数にアクセス
print(luffy.num_legs)
print(nami.num_legs)
print(Person.num_legs)
luffy.num_legs = 4
print('######')
print(luffy.num_legs)
print(nami.num_legs)
Person.num_legs = 3
print('######')
print(luffy.num_legs)
print(nami.num_legs)
