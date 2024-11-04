# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025 - 385 = 2640
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# nums = 10
nums = 100
sum_squared = 0
squares_sum = 0

for i in range(nums+1):
    sum_squared += i
    squares_sum += i**2
sum_squared = sum_squared**2

print(sum_squared - squares_sum)

