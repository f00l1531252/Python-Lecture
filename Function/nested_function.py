msg = 'I am global'


def outer():
    # global msg
    msg = 'I am outer'

    def inner():
        # nonlocal msg
        msg = 'I am inner'
        print(msg)
    inner()
    print(msg)


outer()
print(msg)