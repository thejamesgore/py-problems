print('hello world')

# variables

x = 1           # int
y = 2.5         # float
name = 'John'   # string
is_cool = True  # boolean
is_not_cool = False  # boolean

# Multiple assignment

x, y, name, is_cool = (1, 2.5, 'John', True)

print(x, y, name, is_cool)


# Casting

x = str(x)
y = int(y)
z = float(y)

print(type(x), x)
print(type(y), y)
print(type(z), z)


name = 'James'
age = 37

# strings
# concatenate
print('Hello, my name is ' + name + '. I am ' + str(age))

# String formatting

# Positoinal arguements
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hey my name is {name} and I am {age}')

s = 'hello world'

# Capitalize string
print(s.capitalize())

print(s.upper())

newList = s.split()

print(newList)
