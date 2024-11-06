# 2520  is the smallest number that can be divided by each of
# the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?


dividers = set(range(2, 21))    # No point in dividing by 1.
increment = 2520                # Numbers must be a multiple satisfying the original subset.
number = increment

while True:
    for divider in dividers:
        if number % divider != 0:
            break
    else:
        print(number)
        break
    number += increment

