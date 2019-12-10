import math

#region Conversions
def hex_to_bin(hex_value, bit_seperator = True):
    ''' converts a hex value (as a string) => binary_value
        into a hex value. bit_seperator = True seprates the binary
        return value.
            print(hex_to_binary_converter("30FC401"))
            >>> 0011000011111100010000000001 
            print(hex_to_binary_converter("30FC401",True))
            >>> 0011 0000 1111 1100 0100 0000 0001    
    '''
    hex_bin_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
        '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

    binary_number_list = []
    for char in hex_value:
        for key, value in hex_bin_dict.items():
            # print(f"key: {key}, value: {value}")
            if char.title() == key:
                binary_number_list.append(value + " ")
                # print(value)
    if bit_seperator:
        return str().join(binary_number_list)
    else:
        return str().join(binary_number_list).replace(' ','')


def bin_to_hex(binary_value):
    ''' converts a binary value (as a string) => hex_value
        into a hex value.
            print(binary_to_hex_converter("0011000011111100010000000001"))
            >>> 30FC401    
    ''' 
    hex_bin_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
            '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
    
    n = 4
    hex_value_list = []
    for char in [binary_value[i:i+n] for i in range(0, len(binary_value), n)]:
        for key, value in hex_bin_dict.items():
            # print(f"key: {key}, value: {value}")
            if char == value:
                hex_value_list.append(key)
                # print(value)
    return str().join(hex_value_list)


def bin_to_dec(binary_number):
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
#endregion Conversions


#region Formulas
def perc_dif(original_value, new_value, round_value = 0):
    '''Shows difference between original_value and new_value
       as a percentage, decimal places rounded to the round_value (defaults as 0)
       perc_diff(10,11)
       >>>10.0
    '''
    if round_value == 0:
        return (new_value-original_value)/original_value * 100
    else:
        return round((new_value-original_value)/original_value * 100, round_value)


def percentage_of(numerator, denominator , round_value = 0):
    '''Shows percentage_of between original_value and new_value
        as a percentage, decimal places rounded to the round_value (defaults as 0)
        percentage_of(50,120)
    >>>60.0
    '''
    if round_value == 0:
        return (numerator/denominator) * 100
    else:
        return round((numerator/denominator) * 100, round_value)


def value_by_perc(percentage, value, round_value = 0):
    '''calculates the new value from a percantage of the original
        value , decimal places rounded to the round_value (defaults as 0)
        value_by_perc(75,800)
    >>>600
    '''    
    if round_value == 0:
        return (percentage/100) * value
    else:
        return round((percentage/100) * value, round_value)
#endregion Formulas

def time_of_travel(distance, speed):
    return (distance/speed)*60

def average_speed(distance, time):
    return distance/time

#region averages, quartile ranges & Standard Deviation
def mean_value(value_list):
    return sum(value_list)/(len(value_list))


def median_value(value_list):
    value_list.sort()
    if len(value_list) % 2 == 0:
        return mean_value([value_list[round(len(value_list)//2)],value_list[(round(len(value_list)//2)-1)]])
    else:
        return value_list[round(len(value_list)//2)]


def range_value(value_list):
    return max(value_list)-min(value_list)


def lower_quartile(value_list):
    value_list.sort()
    if len(value_list) % 2 == 0:
        return median_value(value_list[:len(value_list)//2])
    else:
        value_list.remove(value_list[round(len(value_list)//2)-1])
        return median_value(value_list[:len(value_list)//2])  

def higher_quartile(value_list):
    value_list.sort()
    if len(value_list) % 2 == 0:
        return median_value(value_list[len(value_list)//2:])
    else:
        value_list.remove(value_list[round(len(value_list)//2)-1])
        return median_value(value_list[len(value_list)//2:]) 


def interquartile_range(value_list):
    return higher_quartile(value_list) - lower_quartile(value_list)


def std_dev(value_list):
    m = mean_value(value_list)
    deviations = [m - int(d) for d in value_list]
    sqr_d = [d*d for d in deviations]
    sqr_m = mean_value(sqr_d)
    return math.sqrt(sqr_m)

def Summary(value_list):
    size = len(value_list)
    mv = mean_value(value_list)
    mdv = median_value(value_list)
    rv = range_value(value_list)    
    sd = std_dev(value_list)
    iqr = interquartile_range(value_list)
    hq = higher_quartile(value_list)
    lq = lower_quartile(value_list) 
    print(f"min: {min(value_list)}\nmax: {max(value_list)}")
    print(f"mean: {mv}\nmedian: {mdv}\nrange: {rv}")
    print(f"lower quartile: {lq}\nhigher quartile: {hq}\ninter quartile range: {iqr}")
    print(f"standard deviation: {sd}")
    print(f"size of data set: {size}")
#endregion
# my_list = [51,60,60,60,70,70,70,70,75,75,75,75,75,75,75,76,80,80,80,80,85,90,90,90,90,90,95,95,99,99]
my_list_2 = [8,3,2,6,4,1,5,7]
my_list_3 = [321,321,350,350,354,367,367,367,378,378,387,387,398,398,625]

# my_list_4 = [1,2,4,6,7]
print(Summary(my_list_3))
# print(value_by_perc(10,600))
# print(percentage_of(10,12))
# print(perc_dif(100,80))
