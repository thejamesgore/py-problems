# A module is basically a file containing a set of functions 
# to include in your application. There are coe python modules, 
# modules you can install using pip package manager including django as well as custom modules

# import in modules
from validator import validate_email
import datetime
import time

# importing in object from modules
from datetime import date 

# pip module
# from camelcase import CamelCase




today = datetime.date.today()
timestamp = time.time()

day = date.today()



print(today)
print(f'the date imported from date is {day}')
print(timestamp)



# import custom module

email = 'test@test.com'
badEmail= 'test#test.com'

if validate_email(email):
    print(f'Email ({email}) is valid')
else:
    print(f'Email ({email}) is invalid')

if validate_email(badEmail):
    print(f'Email ({badEmail}) is valid')
else:
    print(f'Email ({badEmail}) is invalid')