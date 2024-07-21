# Write a Prime Number Program with following features/functions/methods:
# Determines if an integer is prime or composite
# Generates the nth prime (2 is the 1st prime number)
# Generates the prime factorization of a number 24 = [2, 2, 2, 3]
# Generates the first prime number greater than or equal to a given integer
# Identifies the greatest common factor of two numbers using prime factorization

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    guess = 1
    while count < n:
        guess += 1
        if is_prime(guess):
            count += 1
    return guess

def prime_factorization(n):
    factors = []
    guess = 2
    while n > 1:
        if n % guess == 0:
            factors.append(guess)
            n //= guess
        else:
            guess += 1
    return factors

def next_prime(n):
    guess = n
    while True:
        guess += 1
        if is_prime(guess):
            return guess
        
def greatest_common_factor(a, b):
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)
    common_factors = []
    for factor in factors_a:
        if factor in factors_b:
            common_factors.append(factor)
            factors_b.remove(factor)
    return common_factors

