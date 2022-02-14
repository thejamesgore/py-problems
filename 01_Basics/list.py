#  a collection which is ordered and changeable. Allows duplicate members

# create a list
numbers = [1, 2, 4, 5]
fruits = ['apples', 'ornages', 'Grapes', 'Pears']

# Use a constructor to create a list

numbers2 = list((6, 7, 8, 9))

print(numbers, numbers2)

# get value from list
print(fruits[0])

# get length of list

print(len(fruits))

if len(fruits) == 4:
    print('true')

# Append to list
fruits.append('Mangos')

fruits.remove('ornages')
fruits.append('oranges')

print(fruits)

fruits.insert(2, 'banana')

print(fruits)

fruits.pop(2)

print(fruits)

fruits.reverse()

print(fruits)

# sort makes alphabetical

fruits.sort()

print(fruits)


# change value

fruits[1] = 'Blueberries'

print(fruits)


print(fruits[1:3])

