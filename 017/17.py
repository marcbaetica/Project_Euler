# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3+3+5+4+4=19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
 


numbers = list(range(1, 10))
alpha = ['one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']

conversion_table = dict(zip(numbers, alpha))

numbers = list(range(11, 20))
alpha = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen']
for i in range(len(numbers)):
    conversion_table[numbers[i]] = alpha[i]

numbers = list(range(10, 91, 10))
alpha = ['ten', 'twenty', 'thirty', 'forty', 'fifty',
         'sixty', 'seventy', 'eighty', 'ninety']
for i in range(len(numbers)):
    conversion_table[numbers[i]] = alpha[i]

conversion_table[1000] = 'onethousand'


def convert_double_digit(n_str):
    if n_str[0] == '1' or n_str[1] == '0':
        return conversion_table[int(n_str)]
    else:
        return f'{conversion_table[int(n_str)//10*10]}{conversion_table[int(n_str[1])]}'


def convert_triple_digit(n_str):
    if n_str[1:] == '00':
        return f'{conversion_table[int(n_str[0])]}hundred'
    elif n_str[1] == '0':
        return f'{conversion_table[int(n_str[0])]}hundredand{conversion_table[int(n_str[2])]}'
    return f'{conversion_table[int(n_str[0])]}hundredand{convert_double_digit(n_str[1:])}'


def get_alpha_value(n):
    n_str = str(n)
    length = len(n_str)
    if length == 1:
        return conversion_table.get(n)
    elif length == 2:
        return convert_double_digit(n_str)
    elif length == 3:
        return convert_triple_digit(n_str)
    return conversion_table[1000]



# max_num = 5
max_num = 1000
count = 0
for i in range(1, max_num+1):
    count += len(get_alpha_value(i))
print(count)

# print(get_alpha_value(342))
# print(len(get_alpha_value(342)))
# 
# print(get_alpha_value(115))
# print(len(get_alpha_value(115)))


# def print_numbers(nums):
#     for num in nums:
#         print(num, get_alpha_value(num))
# 
# numbers = [0, 1, 9, 10, 14, 20, 30, 35, 89, 90, 99, 100,
#            101, 110, 114, 156, 244, 500, 999, 1000]
# print_numbers(numbers)

# for i in range(1, 1001):
#     if 'None' in get_alpha_value(i):
#         print(i)

