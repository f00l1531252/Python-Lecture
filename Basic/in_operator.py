fruits = ['apple', 'banana', 'peach', 'orange']
print('apple' in fruits)
print('lemon' in fruits)
print('lemon' not in fruits)

print('a' in 'hello world')

print('###Challenge###')
favorite_fruit = input('好きなフルーツを入力してください')
if favorite_fruit in fruits:
    fruits.remove(favorite_fruit)
    print(fruits)
else:
    fruits.append(favorite_fruit)
    print(fruits)