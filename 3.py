# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143?


primes = []

def is_prime(n):
    for i in range(2, n-1):
        print(i)
        if n%i==0:
            print(f'{n} {i}')
            return False
        return True


def find_primes(number):
    for i in range(1, number):
        print(f'Computing for {i}:')
        if is_prime(i):
            primes.append(i)


# number = 13195
number = 15
find_primes(number)
print(primes)

