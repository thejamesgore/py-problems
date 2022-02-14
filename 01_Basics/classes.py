# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. 
# Almost everyting in python is an object

# Create class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Init user object
james = User('James', 'james@gmail.com', 33)

# Accessing elements of the user object
print(f'the name for the user is {james.name}')
print(f'the email for the user is {james.email}')
print(f'the age for the user is {james.age}')

james.has_birthday()
print(james.greeting())

# Extending classes

class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name}, I am {self.age}, and my balance is {self.balance}'

# Init a customer object

marco = Customer('Marco', 'MrM@gmail.com', 25)

print(marco.greeting())

marco.set_balance(25)

print(marco.greeting())