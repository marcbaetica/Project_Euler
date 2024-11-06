# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
 
import math


def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True


# n_th = 6
n_th = 10001
i = 2
primes_count = 1

while True:
    i += 1
    if is_prime(i):
        primes_count +=1
    if primes_count == n_th:
        break

print(i)

