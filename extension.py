import copy
from fractions import Fraction

from system_of_equations import solve_system_of_equations,solve_system_of_equations_2
from cubic_ring import CubicRing

# if only one basis is changed
# this must work for any case of extension
def compute_updated_a_b_c_d(ring,prime):

    tilde_a = prime * ring.a
    tilde_b = ring.b - 3 * ring.beta * ring.a
    tilde_c = (3 * ring.beta * ring.beta * ring.a - 2 * ring.beta * ring.b + ring.c) / prime
    tilde_d = (-ring.beta * ring.beta * ring.beta * ring.a + ring.beta * ring.beta * ring.b - ring.beta * ring.c + ring.d) / (prime * prime)
    return tilde_a,tilde_b,tilde_c,tilde_d

def compute_updated_a_b_c_d_triangular(ring,prime):

    tr = (3 * ring.alpha + ring.beta * ring.b + ring.gamma * ring.c)/prime
    m_2_2 = (-ring.a * ring.a * ring.beta * ring.beta * ring.d + 3 * ring.alpha * ring.alpha + ring.a * ring.b * ring.beta * ring.d * ring.gamma + ring.a * ring.beta * ring.beta * ring.c - 2 * ring.a * ring.beta * ring.d * ring.gamma + 2 * ring.alpha * ring.b * ring.beta + ring.b * ring.beta * ring.c * ring.gamma + ring.b * ring.d * ring.gamma * ring.gamma + 2 * ring.alpha * ring.c * ring.gamma)/(prime*prime)
    det = (ring.alpha * ring.alpha * ring.alpha + ring.a * ring.a * ring.beta * ring.beta * ring.beta * ring.d - ring.a * ring.b * ring.beta * ring.beta * ring.gamma * ring.d - ring.gamma * ring.a * ring.b * ring.beta * ring.beta * ring.d + ring.a * ring.beta * ring.beta * ring.c * ring.c * ring.gamma + ring.a * ring.alpha * ring.beta * ring.beta * ring.c - 2 * ring.a * ring.beta * ring.c * ring.gamma * ring.gamma * ring.d + ring.gamma * ring.gamma * ring.gamma * ring.a * ring.d * ring.d - 3 * ring.a * ring.alpha * ring.beta * ring.gamma * ring.d + ring.gamma * ring.gamma * ring.b * ring.b * ring.beta * ring.d + ring.alpha * ring.alpha * ring.b * ring.beta + ring.alpha * ring.b * ring.beta * ring.c * ring.gamma + ring.gamma * ring.gamma * ring.alpha * ring.b * ring.d + ring.alpha * ring.alpha * ring.c * ring.gamma)/(prime*prime*prime)

    tilde_a = 1
    tilde_b = -2 * tr
    tilde_c = (tr * tr) + m_2_2
    tilde_d = det - tr * m_2_2
    return tilde_a,tilde_b,tilde_c,tilde_d



def create_an_extended_ring(ring,prime):
    a,b,c,d = compute_updated_a_b_c_d(ring,prime)
    tilde_ring = CubicRing(a,b,c,d)

    # TODO: update basis (incorrect while swapping)

    #tilde_ring.third_basis[2] = Fraction(1/p * ring.third_basis[2])
    #tilde_ring.third_basis[1] = Fraction(1/p * ring.third_basis[1] + ring.beta/p)
    #tilde_ring.third_basis[0] = Fraction(1/p*ring.third_basis[0] - (ring.beta*ring.beta*ring.a - ring.beta*ring.b)/p + ring.beta/p*ring.second_basis[0] )

    #tilde_ring.second_basis[0] = ring.second_basis[0] - ring.beta*ring.a
    return tilde_ring

def create_an_extended_ring_triangular(ring,prime):
    a,b,c,d = compute_updated_a_b_c_d_triangular(ring,prime)
    tilde_ring = CubicRing(a, b, c, d)

    # TODO: update basis (incorrect while swapping)

    #tilde_ring.third_basis[2] = Fraction(1/p * ring.third_basis[2])
    #tilde_ring.third_basis[1] = Fraction(1/p * ring.third_basis[1] + ring.beta/p)
    #tilde_ring.third_basis[0] = Fraction(1/p*ring.third_basis[0] - (ring.beta*ring.beta*ring.a - ring.beta*ring.b)/p + ring.beta/p*ring.second_basis[0] )

    #tilde_ring.second_basis[0] = ring.second_basis[0] - ring.beta*ring.a
    return tilde_ring

def extend_with_prime_2(ring, prime):
    for alpha in range (0,prime):
        for beta in range (0,prime):
            if solve_system_of_equations(ring.a, ring.b, ring.c, ring.d, alpha, beta, prime):
                ring.alpha, ring.beta = alpha, beta
                return

def extend_with_prime_2_triangular(ring,prime):
    for alpha in range (0,prime):
        for beta in range (0,prime):
            for gamma in range(0,prime):
                if alpha == 0 and beta == 0 and gamma == 0: continue
                if solve_system_of_equations_2(ring.a, ring.b, ring.c, ring.d, alpha, beta, gamma, prime):
                    ring.alpha, ring.beta, ring.gamma = alpha, beta, gamma
                    return

def try_extend(ring,prime):
    #extend changing one basis
    extend_with_prime_2(ring,prime)
    if ring.alpha != -1 or ring.beta != -1:
        return create_an_extended_ring(ring,prime)

    ring.swap_basis_elements()
    extend_with_prime_2(ring,prime) # second chance
    if ring.alpha != -1 or ring.beta != -1:
        return create_an_extended_ring(ring,prime)

    #extend changing two basis
    extend_with_prime_2_triangular(ring,prime)
    if ring.alpha != -1 or ring.beta != -1 or ring.gamma != -1:
        #there are some extra conditions
        new_ring = create_an_extended_ring_triangular(ring,prime)
        #new_ring.swap_basis_elements()
        return new_ring

    return None