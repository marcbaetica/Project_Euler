# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

divide_by = [3, 5]
threshold = 1000

numbers = []
for num in range(threshold):
    if any([num for divisor in divide_by if num%divisor==0]):
        numbers.append(num)

print(sum(numbers))

