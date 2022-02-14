# a loop is used for iterating over a sequence that is either a list, tuple, a dict, a set, or string

people = ['James', 'John', 'Jane', 'Janet']

for person in people:
    print(f'Current person:{person}')

    print('>>>>>>>>>>>>>')
    print('>>>>>>>>>>>>>')

# Break out of a loop - stops loop

for person in people:
    if person == 'Jane':
        break
    print(f'Current person:{person}')

print('>>>>>>>>>>>>>')
print('>>>>>>>>>>>>>')


# Continue in loops - Skips element

for person in people:
    if person == 'Jane':
        continue
    print(f'Current person:{person}')


print('>>>>>>>>>>>>>')
print('>>>>>>>>>>>>>')


# Range

for i in range(len(people)):
    print(people[i])

for i in range(0, 7):
    print(f'The current number is {i}')

# While loops execute a set of statements as long as a condition is true

count = 0
while count < 10:
    count = count + 1
    print(f'The count is {count}')