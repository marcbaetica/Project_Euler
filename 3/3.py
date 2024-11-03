# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?


def is_prime(num):  # Can only be divided by 1 and by itself.
    for i in range(2, int(num/2+1), 1):
        if num%i==0:
            return False
    return True


def find_primes(max_num):
    for i in range(2, int(max_num/2)+1):
        if is_prime(i):
            yield i
    print('Reached the end of possible prime factors.')


# number = 13195
number = 600851475143

primes = find_primes(number)
while True:
    prime = next(primes)
    if number%prime == 0:
        number = number/prime
        print(f'Divided by prime number {prime}. New number is now: {number}')
        if number == 1:
            break

print(prime)

