def square(num):
    return num * num


f = square
print(type(f))
print(f)
print(f(10))

function_list = [1, 2, f]
print(function_list[-1](10))

# 関数も引数として渡せる
def execute_func(func, parm):
    return func(parm)


print(execute_func(f, 10))

# 関数をreturnする
def return_func():
    def inner_func():
        print('This is an inner function')
    return inner_func

f = return_func()
print(type(f))
print(f)
f()

print('###################')
# closure　状態をキープした関数を作ることができる
# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four)
print(power_four(2))

print('##################')
#　状態が動的
def average():
    nums = []
    def inner_average(num):
        nums.append(num)
        print(f'リスト{nums}')
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
print(average_nums)
print(average_nums(10))
print(average_nums(20))
print(average_nums(30))
print(average_nums(40))