fruits = ['apple', 'orange', 'banana']
print(id(fruits))
fruits.append('peach')
print(id(fruits))

fruit = 'apple'
print(id(fruit))
fruit += 'pen'
print(id(fruit))


text = ''
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '_' + str(i)
print(text)


text_list = []
for i in range(1, 11):
    text_list.append(str(i))
text = '_'.join(text_list)
print(text)

text_list = [str(i) for i in range(1, 11)]
print(text_list)
text = '_'.join(text_list)
print(text)