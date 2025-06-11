from chain_of_cubic_rings import ChainOfCubicRings
from cubic_ring import CubicRing
from extension import try_extend
from system_of_equations import solve_system_of_equations_2

chain = ChainOfCubicRings()

first_ring = CubicRing(1 , 0 , 1 , 0)
print(first_ring.get_discriminant())
chain.add_ring(first_ring)

last_ring = chain.get_last_ring()
new_ring = try_extend(last_ring,17)
#print(new_ring.get_discriminant())
#chain.add_ring(new_ring)
#chain.get_all_rings()

'''
while last_ring.get_discriminant()%4 == 0 and last_ring.get_discriminant() != 0:
    new_ring = try_extend(last_ring)

    if new_ring is not None:
        #new_ring.print_numbers()
        chain.add_ring(new_ring)
    else:
        break

    last_ring = chain.get_last_ring()

chain.get_all_rings()
'''

