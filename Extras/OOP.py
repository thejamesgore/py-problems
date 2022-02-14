# Creating a class
class employee:

    def __init__(self, firstname, lastname, salary): # initialising the class
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." +self.lastname + "@company.com"

    def giveRaise(self, salary):

        self.salary = salary


class developer(employee):

    def __init__(self, firstname, lastname, salary, programming_languages):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = programming_languages

    def addLanguage(self, lang):
        self.prog_langs += [lang]

employee1 = employee('Jack', "Whiskers", 60000)

print(employee1.salary)

employee1.giveRaise(100000)

print(employee1.salary)

dev1 = developer("Joe", "Smith", "80000", ["Python", "C"])

print(dev1.salary)

dev1.giveRaise(125000)

dev1.addLanguage("Javascript")

print(dev1.prog_langs)