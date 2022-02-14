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

# remove specific item
mylist.remove("apple")

# reverse the list
mylist.reverse()

# sort
numbers = [1,4,3,6,8,2,5,11,333]

numbers.sort() # mutates data

new_list = sorted(numbers) # does not mutate original list

#  repeats elements in list
multiplied_list = [0] * 5 
print(multiplied_list)

# SLICING - [start index : end index] 

sliced = [1,2,3,4,5,6,7,8,9]

a = sliced[1:5]

print(a)

# 

b = sliced[::2] # only includes every 2 items

print(b)

# when copying use append. if you edit an assigned list the original gets editted too

newList = sliced

print(sliced)
newList.pop() # Also edits sliced list
print(sliced)

# list comprehension!

newly_sliced = [x * x for x in sliced]

print(newly_sliced)