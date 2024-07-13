def power(exponent):

    return lambda base: base ** exponent



power_four = power(4)
print(power_four(2))


numbers = [55, 13, 64, 98, 123]


def filter_func(num):
    if num % 2 == 0:
        return False
    else:
        return True




for num in numbers:
    print(filter_func(num))

print('#######')
filter_num = filter(lambda num: num % 2, numbers)
print(list(filter_num))

