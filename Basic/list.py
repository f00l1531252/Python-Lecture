fruits = ['banana', 'apple', 'melon', 'orange']
various_list = ['strings', 1, 3.4, True, fruits]

print(fruits)
print(various_list)
print(fruits[2])
print(various_list[-1][0])

print('hello world'[4])
print('#########')
print(fruits)

fruits.append('peach')
print(fruits)

fruits.insert(3, 'banana')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(len(fruits))

print('#####')
print([1, 2, 3] + [4, 5, 6])
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
a += b
print(a)
a.append(b)
print(a)
