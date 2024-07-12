call_count = 0


def print_count():
    global call_count
    call_count += 1
    print(f'関数１:{call_count}回目')


def print_count2():
    global call_count
    call_count += 1
    print(f'関数２:{call_count}回目')


print_count()
print_count()
print_count2()
