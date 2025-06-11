from discriminant import compute_discriminant
from extension import try_extend
from prime_factorization import prime_factors, is_squaree_free, no_first_power_of_prime
import collections
from cubic_ring import CubicRing

# find a cubic ring with a squaree-free discriminant
count = 0
count_non_zero_discriminant = 0

def gererate_cubic_ring_with_squaree_free_discriminant():
    cubic_rings = []
    for a in range(0,8):
        for b in range(0,8):
            for c in range(0,8):
                for d in range(0,8):
                    discriminant = compute_discriminant(a,b,c,d)
                    primes = prime_factors(abs(discriminant))
                    if is_squaree_free(primes) and discriminant != 0:
                        cubic_rings.append(CubicRing(a,b,c,d))

    return cubic_rings

def gererate_cubic_ring_with_discriminant_one():
    cubic_rings = []
    r = 128
    for a in range(1,r):
        for b in range(0,r):
            for c in range(0,r):
                for d in range(0,r):
                    discriminant = compute_discriminant(a, b, c, d)
                    if discriminant == 1:
                        print(a,b,c,d)

def gererate_cubic_ring_with_no_prime_with_power_one():
    cubic_rings = []
    for a in range(0,16):
        for b in range(0,16):
            for c in range(0,16):
                for d in range(0,16):
                    discriminant = compute_discriminant(a, b, c, d)
                    primes = prime_factors(abs(discriminant))
                    if no_first_power_of_prime(primes) and discriminant != 0:
                        cubic_rings.append(CubicRing(a,b,c,d))
    return cubic_rings

def generate_cubic_rings_non_squaree_free_non_extending():
    cubic_rings = gererate_cubic_ring_with_no_prime_with_power_one()
    new_cubic_rings = []

    for cubic_ring in cubic_rings:
        #print("checking")
        #cubic_ring.print_numbers()
        found = True
        discriminant = cubic_ring.get_discriminant()
        prime_decomposition_of_discriminant = prime_factors(abs(discriminant))
        unique_primes = set(prime_decomposition_of_discriminant)
        for p in unique_primes:
            # ignore primes that occurs once
            if prime_decomposition_of_discriminant.count(p) == 1:
                continue
            if try_extend(cubic_ring,p) is not None:
                found = False
                break

        if found:
            new_cubic_rings.append(cubic_ring)
            #cubic_ring.print_numbers()
            #print("yes")

    print(len(new_cubic_rings))
    for new_ring in new_cubic_rings:
        new_ring.print_numbers()

gererate_cubic_ring_with_discriminant_one()



#among those generate those that does not admit even one extension

'''
def generate_cubic_ring_a_a():
    cubic_rings = []
    for i in range(1,64):
        #if i%4 != 0:
        linked_lst = collections.deque()
        linked_lst.append(CubicRing(i, i, 64-i, 64-i))
        cubic_rings.append(linked_lst)

    return cubic_rings

def generate_cubic_ring_b_b():
    cubic_rings = []
    for i in range(1,8):
        linked_lst = collections.deque()
        linked_lst.append(CubicRing(0, i, 8, 0))
        cubic_rings.append(linked_lst)

    return cubic_rings


def generate_cubic_rings_with_discriminant_divisible_by_four():
    l = 0
    r = 16
    p = 2

    cubic_rings = []

    for a in range(l,r):
        for b in range(l,r):
            for c in range(l,r):
                for d in range(l,r):
                    # cannot extend whatsoever
                    if compute_discriminant(a, b, c, d) % 4 != 0 or compute_discriminant(a,b,c,d) == 0:
                        continue
                    linked_lst = collections.deque()
                    linked_lst.append(CubicRing(a,b,c,d))
                    cubic_rings.append(linked_lst)

    return cubic_rings
'''