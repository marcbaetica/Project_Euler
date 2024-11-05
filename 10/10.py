# The sum of the primes below 10 is 2+3+5+7=17.
# 
# Find the sum of all the primes below two million.


import math


def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True


def generate_prime():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


sum = 0
# threshold = 10
threshold = 2*10**6


primes = generate_prime()
while True:
    prime = next(primes)
    if prime > threshold:
        break
    sum += prime
    # print(f'Found new prime number {prime}. New sum is: {sum}')
print(sum)

