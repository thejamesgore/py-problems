# Dictionaries are unordered collections, changeable and indexed. No duplicate members.

# create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
}
# create a dict using a constructor
person2 = dict(first_name='Sara', last_name='Williams')

print(person, 'the type is', type(person))


print(person2)

# Get values from dict
print(person['first_name'])

print(person.get('last_name'))

# Add key/value

person['height'] = '180cm'

print(person)

print(person['height'])

# Get dict keys

print(person.keys())

# get items

print(person.items())

# copy a dict

person3 = person.copy()
person3['city'] = 'Boston'

print(person3['city'])

# delete item

del(person['first_name'])

print(person)

person.pop('age')

print(person)

print(len(person))

# list of dict

people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]


print('This is the people list dict', people)

# get name of first person

print(people[0]['name'])
