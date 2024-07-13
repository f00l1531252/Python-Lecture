# 関数に機能を付属する

def greeting(func):
    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Nice to meet you')
    return inner


@greeting
def say_name(name):
    print(f"I'm {name}")


# say_name = greeting(say_name)
print(say_name)
say_name('aki')


@greeting
def say_name_and_origin(name, origin):
    print(f"'I'm {name}, I'm from {origin}")


say_name_and_origin('aki', 'Gifu')
