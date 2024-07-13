class Person:
    def __init__(self, name):
        self.name = name
        self.__mymethod()

    def mymethod(self):
        print('Person method is called')

    __mymethod = mymethod


class Baby(Person):
    def mymethod(self):
        print('Baby method is called')


taro = Baby('Taro')
aki = Person('Aki')
print(taro.name)
print(aki.name)
taro.mymethod()
aki.mymethod()
print(dir(taro))