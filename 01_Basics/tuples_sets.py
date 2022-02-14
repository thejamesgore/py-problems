# A tuple is a collection which is ordered and unchangeable. allows duplicate members

#  Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value needs trailing comma
fruits2 = ('Apples',)

print(fruits2, type(fruits2))

print(fruits[2])

# Get length
print(len(fruits))

print('<<< ON TO SETS >>>')

# Sets are a collection which is unordered and unindexed, no duplicate members.

fruits_set = {'Apples', 'Oranges', "Mango"}

# Check if in set

print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Add a duplicate
fruits_set.add('Grape')
print(fruits_set)

# Remove from set

fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()

print(fruits_set)
