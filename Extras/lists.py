list = [1,2,3,4,5,6,7]

even_list = [ x for x in list if x % 2 == 0]

print(list)
print(even_list)

square_list = [x ** 2 for x in list]
print(square_list)