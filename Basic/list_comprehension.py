square_list = []

for i in range(10):
    square_list.append(i ** 2)

print(square_list)


square_list2 = [i ** 2 for i in range(10)]
print(square_list2)

square_list3 = [i ** 2 for i in range(10) if i % 2 == 0]
print(square_list3)