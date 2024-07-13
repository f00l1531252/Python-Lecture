class MyClass:
    def __str__(self):
        return 'MyClassの__str__'
    # pass

mc = MyClass()
print(mc)
print(mc.__str__())