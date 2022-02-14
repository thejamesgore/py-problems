# Create a program which converts weight

def convert_weight():
    weight = float(input(f"Enter the weight you wish to convert: "))
    system = input(f"Is the weight in (K)g or (L)bs? ").upper()

    if system == 'L':
        weight = weight / 2.2
        print(f"The weight in kgs is {weight}")
    elif system == 'K':
        weight = weight * 2.2
        print(f"The weight in lbs is {weight}")

convert_weight()