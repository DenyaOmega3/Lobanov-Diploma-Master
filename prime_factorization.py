import math

def is_squaree_free(prime_decomposition):
    individual_primes = set(prime_decomposition)
    for prime in individual_primes:
        if prime_decomposition.count(prime) > 1:
            return False
    return True

def no_first_power_of_prime(prime_decomposition):
    individual_primes = set(prime_decomposition)
    for prime in individual_primes:
        if prime_decomposition.count(prime) == 1:
            return False
    return True


def prime_factors(n):
    if n == 0:
        return [0]
    #number = ""
    factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        #number+="2*"
        factors.append(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            #number+=(str(i)+"*")
            factors.append(i)
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        #number +=(str(n)+"*")
        factors.append(n)

    return factors
    #return number