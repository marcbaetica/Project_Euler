# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palidrome(num):
    return num == int(str(num)[::-1])


biggest_number = 0
for x in range(999, 1, -1):
    for y in range(999, 1, -1):
        if is_palidrome(x*y):
            if x*y > biggest_number:
                biggest_number = x*y
                print(f'Found new larger palidrome for: {x} * {y} = {biggest_number}')

