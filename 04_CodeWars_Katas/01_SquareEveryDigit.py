# Square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    # convert number to string
    num_as_string = str(num)

    # split string into a list
    num_list = list(num_as_string)
    # print(num_list)

    #  convert each item back to integer
    list_as_int = list(map(int, num_list))
    # print(list_as_int)

    # iterate over list and square every number
    for i in list_as_int:
        i = i**2
        print(i)

    

    # join each item in list
    # string = ''
    # string.join(list_as_int)
    # print(string)
    

square_digits(9119)