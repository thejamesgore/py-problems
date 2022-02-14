# Python has functions for creating, reading, updating, and deleting files.

# Opena  file

myFile = open('myfile.txt','w')

# Get info on file

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Wrting to file

myFile.write('I love bananas')
myFile.write(' and python')
myFile.close()

# Can't write to file if not open
# myFile.write(' and JavaScript')

# Append to file without overwriting data
myFile = open('myfile.txt', 'a')
myFile.write(' and JavaScript')

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)