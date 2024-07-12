def add_one(num):
    print(f'変更前のID:{id(num)}')
    num += 1
    print(f'変更後のID:{id(num)}')
    return num


one = 1
print(id(one))
print(f'関数呼び出し前のoneのID:{id(one)}')
add_one = add_one(one)
print(f'関数呼び出し後のoneのID:{id(one)}')
print(f'関数から返ってきた値のID:{id(add_one)}')


print('############')


def add_fruit(fruits, fruit):
    print(f'変更前のID:{id(fruits)}')
    fruits.append(fruit)
    print(f'変更後のID:{id(fruits)}')
    return fruits


fruits = ['apple', 'banana', 'orange']
print(f'変更前のリスト:{fruits}')
add_fruit(fruits, 'grapes')
print(f'変更後のリスト:{fruits}')




