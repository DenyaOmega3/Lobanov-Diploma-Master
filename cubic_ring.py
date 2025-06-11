from copy import deepcopy

from discriminant import compute_discriminant

class CubicRing:
    def __init__(self,a,b,c,d,second_basis = [0,1,0], third_basis = [0,0,1]):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.second_basis = deepcopy(second_basis)
        self.third_basis = deepcopy(third_basis)

        # parameters for specifying an extension
        self.alpha = -1
        self.beta = -1
        # parameter for specifying an extension with another option
        self.gamma = -1

    def get_discriminant(self):
        return compute_discriminant(self.a,self.b,self.c,self.d)

    def swap_basis_elements(self):
        self.a, self.b, self.c, self.d = self.d, self.c, self.b, self.a
        self.second_basis, self.third_basis = self.third_basis, self.second_basis

    def print_numbers(self):
        print("[",self.a,",",self.b,",",self.c,",",self.d,"],")
        #print("(a,b,c,d) = (",self.a,",",self.b,",",self.c,",",self.d,")")

    def print_basis(self):
        print("First basis: 1")
        print("Second basis: ", self.second_basis[0],"+",self.second_basis[1],"omega_1 + ",self.second_basis[2],"omega_2")
        print("Third basis: ", self.third_basis[0],"+",self.third_basis[1],"omega_1 + ",self.third_basis[2],"omega_2")