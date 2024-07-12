def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4)
print(average)


def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(param1=10, patam2=20, param3=30)

print('#######')
def kwargs_func2(**kwargs):
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)
    param4 = kwargs.get('param4', 4)
    param5 = kwargs.get('param5', 5)
    print(param1, param2, param3, param4, param5)


kwargs_func2(param1=10, param2=20, param3=30)

print('########')
num = (1, 2, 3)
print(*num)

a = {1: 'one', 2:'two'}
b = {3: 'three', 4: 'four'}
c = {**a, **b}
a.update(b)
print(c)
print(d)
print(a)