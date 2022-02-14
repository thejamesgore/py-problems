# Creating a binary search algo and comparing to a basic search algo

# Basic search scans a list in order and checks if an item is equal to the target

# Binary search checks to see if the item is less than, greater than, or equal to the current index
# and then focuses search on that chunk leaving the rest, then repeating this until it finds the item.

def basic_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
    

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    
    if high is None:
        high = len(list) -1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target)

if __name__ == '__main__':
    list = [1, 3, 5, 10, 12]
    target = 10
    print(basic_search(list, target))
    print(binary_search(list, target))