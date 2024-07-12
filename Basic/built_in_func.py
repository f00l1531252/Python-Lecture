hello_type = type('hello')
print(hello_type)

hello_id = id('hello')
print(hello_id)
hello = 'hello'
hello2 = 'hello'
print(id(hello))
print(id(hello2))
world = 'world'
print(id(world))
print(id('world'))
print(hello + ' ' + world)