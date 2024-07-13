class Animal:
    def __init__(self, name):
        self.name = name
        print('Animal init is called')

    def breath(self):
        print(f'{self.name} is breath')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)
        print('dog init is called')


class Cat(Animal):
    pass


class Bird(Animal):
    def fly(self):
        print(f'{self.name} is flying')


pochi = Dog('pochi')
tama = Cat('tama')

print(pochi.name)
print(tama.name)

pochi.breath()