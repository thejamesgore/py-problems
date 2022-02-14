x = 10
y = 5
z = 1

# Comparison Operators

# simple if, will not print if not true
if x > y:
    print(f'{x} is greater than {y}')

if z < y:
    print(f'{y} is greater than {z}')
else:
    print(f'{z} is greater than {y}')

# Else if statements

if z < y:
    print(f'{y} is greater than {z}')
elif z == y:
    print(f'{z} is equal to {y}')
else:
    print(f'{z} is greater than {y}')

# Nested if

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x <= 10:
    print(f'{x} (x) is greater than 2 and less than and equal to 10')

if x > 2 or x <= 10:
    print(f'{x} (x) is greater than 2 OR less than and equal to 10')

if x != y:
    print(x)
    print(y)
    print(f'{x} (x) does not equal y')

# Testing values

numbers = [1,2,3,4,5]

# in
if y in numbers:
    print(y in numbers, y)

# not in

if x not in numbers:
    print(x not in numbers, 'x is not in the list numbers and the value is', x)

