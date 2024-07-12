a = 1
b = 1
c = 2
d = a
e = c - a
print(a is b)
print(id(a))
print(id(b))

print(id(a + 1))
print(id(b + 1))

print(a is not c)
print(a+1 is not c)
print(id(c))

print(a is d)
print(b is d)
print(e is d)
print('######')

hello = 'hello'
hello2 = 'he' + 'llo'
print(hello, hello2)
print(hello is hello2)
hello = 'hey'
print(hello is hello2)

print('#####')
nothing = None
print(nothing)
print(nothing is None)