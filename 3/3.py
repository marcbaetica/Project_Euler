# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?


def is_prime(num):  # Can only be divided by 1 and by itself.
    for i in range(2, int(num/2+1), 1):
        if num%i==0:
            return False
    return True


primes = []

# number = 13195
number = 600851475143

for i in range(2, number):
    if is_prime(i):
        # print(i)
        if number%i==0:
            number = number/i
            primes.append(i)
            print(f'Divided by prime number {i}. New number is now: {number}')
            if number == 1:
                break
print(primes[-1])

