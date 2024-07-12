for i in range(4):
    print(i)
print('####')
for i in range(1, 4, 2):
    print(i)

print('####')
for _ in range(5):
    print('hello')

print('###challenge###')
for i in range(1, 51):

    if i % 15 == 0:
        print(f'{i} is FizzBuzz')
    elif i % 3 == 0:
        print(f'{i} is Fizz')
    elif i % 5 == 0:
        print(f'{i} is Buzz')
    else:
        print(i)
