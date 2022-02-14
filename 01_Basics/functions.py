# Create a function
def sayHello(name='Sam'):
    print(f'hello, my name is {name}')


sayHello()
sayHello('James')

# Return values


def getSum(num1, num2):
    total = num1 + num2
    print(total)
    return total


getSum(3, 4)

num = getSum(5, 6)

print(num)

# A lambda function is a small anonymous function
# Can take any number of arguments, but can only have one expression

getSum = lambda num1, num2 : num1+num2 

print(getSum(10,2))