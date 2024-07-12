age = 30


def print_age():
    age = 20
    print(f'私は{age}歳です')

print_age()
print(age)


def print_age2():
    global age
    age = 15
    print(f'私は{age}歳です')

print_age2()
print(age)