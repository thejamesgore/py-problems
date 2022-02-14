birth_year = input('Enter your birth year: ')
# code will error if you don't convert birth_year from a string to an integer
age = 2020 - int(birth_year)
print(f'So you are {age}')

# convert to int
int()

# convert to float
float()

# convert to bool
bool()

# convert to str
str()

print('We are going to calculate the sum of two numbers')
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

def sum(num1, num2):
    sum = float(num1) + float(num2)
    return sum

print('The sum of those two numbers are' ,sum(num1, num2))