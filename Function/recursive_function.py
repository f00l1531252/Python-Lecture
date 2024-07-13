def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(10))


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))


def fibonacci2(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


print(fibonacci2(6))

import time

before = time.time()
for i in range(30):
    print(i, fibonacci2(i))
after = time.time()
print(after-before)
