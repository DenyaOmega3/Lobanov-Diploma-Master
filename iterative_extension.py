from chain_of_cubic_rings import ChainOfCubicRings
from cubic_ring import CubicRing
from prime_factorization import prime_factors
from extension import try_extend

chain = ChainOfCubicRings()


first_ring = CubicRing(3 , 3 , 3 , 1)
chain.add_ring(first_ring)
current_discriminant = first_ring.get_discriminant()

if current_discriminant != 0:
    last_ring = chain.get_last_ring()
    prime_factors_of_discriminant = prime_factors(abs(current_discriminant))
    while len(prime_factors_of_discriminant) != 0:
        smallest_prime = prime_factors_of_discriminant[0]

        if current_discriminant%(smallest_prime*smallest_prime) != 0:
            # no extension with this prime
            prime_factors_of_discriminant.remove(smallest_prime)
            continue

        new_ring = try_extend(last_ring,smallest_prime)
        if new_ring is not None:
            chain.add_ring(new_ring)

            #update discriminant and prime factors
            new_current_discriminant = new_ring.get_discriminant()
            quotient = current_discriminant/new_current_discriminant
            factor_quotient = prime_factors(abs(quotient))
            for q in factor_quotient:
                prime_factors_of_discriminant.remove(q)
            current_discriminant = new_current_discriminant
        else:
            while smallest_prime in prime_factors_of_discriminant:
                prime_factors_of_discriminant.remove(smallest_prime)
                #current_discriminant/=smallest_prime
            # remove factors

        last_ring = chain.get_last_ring()

chain.get_all_rings()