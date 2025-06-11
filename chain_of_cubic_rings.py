import collections

class ChainOfCubicRings:
    def __init__(self):
        self.chain = collections.deque()

    def add_ring(self,ring):
        self.chain.append(ring)

    def get_last_ring(self):
        return self.chain[-1]

    def get_all_rings(self):
        for ring in self.chain:
            ring.print_numbers()
            ring.print_basis()
            print(ring.get_discriminant())
