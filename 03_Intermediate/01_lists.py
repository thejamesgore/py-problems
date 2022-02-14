# Data type that is ordered, mutable, allows duplicate elements

mylist = ["apple", "cheery", "apple"] 

mylist2 = list() # creating an empty list with the list contructor

mylist3 = [5, True, "apple", "apple"] # can take all data types and duplicates

item = mylist3[1] # accesses 2nd item in index
lastItem = mylist3[-1] # can specify negative index to access items from the end of the list.

# Can iterate over list with a loop
for i in mylist3:
    print(i)

#  can check if item is in a list
if "banana" in mylist3:
    print("Yes")
else:
    print("No")

# Can check how many items are in a list
len(mylist)

# Append items
mylist.append("lemon")
print(mylist)

# Insert an item at specific index
mylist.insert(1, 'Blueberry')

# Remove item
lastItem = mylist.pop()