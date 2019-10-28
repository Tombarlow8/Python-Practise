# binary to decimal converter
import math

def binary_to_decimal(binary_number):
    power = 0
    binary_base = 2
    binary_list = []
    # slicing to reverse binary digits and work through each digit increasing the 'power of' each time
    for digit in str(binary_number)[::-1]:
        if int(digit) == 1:
            if power == 0:
                binary_list.append(1)
            else:
                binary_list.append(binary_base**power)
        power += 1
    return sum(binary_list)

print(binary_to_decimal(11110111))

