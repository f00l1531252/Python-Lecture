fruits = ['apple', 'peach', 'banana', 'orange']

for fruit in fruits:
    print(fruit)

for char in 'hello':
    print(char)

# print('###challenge###')
# favorite = input('好きなフルーツを入力してください。')
# for fruit in fruits:
#     if favorite == fruit:
#         print(f'{fruit}は好き')
#     else:
#         print(f'{fruit}は好きじゃない')
#

print('###challenge###')
favorite_fruits_list = []
normal_fruits_list = []
for fruit in fruits:
    choice = input(f'{fruit}は好きですか。(y/n)')
    if choice == 'y':
        favorite_fruits_list.append(fruit)
    else:
        normal_fruits_list.append(fruit)

print(f'好きなフルーツ{favorite_fruits_list}')
print(f'好きではないフルーツ{normal_fruits_list}')


