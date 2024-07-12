fruits_color = {'apple': 'red', 'peach': 'pink', 'banana': 'yellow'}

print(fruits_color)
print(fruits_color['apple'])

fruits_color['lemon'] = 'yellow'
print(fruits_color)

dict_sample = {1: 'one', 'two': 2, 3: [1, 2, 3], 'four': {'inner': 4}}
print(dict_sample['four']['inner'])

colors = {}
colors[1] = 'red'
colors[0] = 'blue'
colors[3] = 'yellow'
print(colors)

print('###########')
for fruit in fruits_color.keys():
    print(fruit)
print('###########')
for color in fruits_color.values():
    print(color)
print('###########')
for x in fruits_color:
    print(x)
print('###########')
for fruit, color in fruits_color.items():
    print(f'{fruit} is {color}')

print('*************')
if 'grapes' in fruits_color:
    print(fruits_color['grapes'])
else:
    print('キーが見つかりません')

print(fruits_color.get('grapes', 'Nothing'))

fruit = input('フルーツの名前を入力してください')
print(fruits_color.get(fruit, 'Nothing'))

fruits_color2 = {'grapes': 'purple', 'kiwi': 'green'}
fruits_color.update(fruits_color2)
print(fruits_color)