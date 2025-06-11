from prime_factorization import prime_factors
from discriminant import discriminant_is_zero

'''
def check_for_extension(a,b,c,d,alpha,beta,p):
    #print("Case when a,b,c,d =", a,b,c,d)
    #print("Extending with alpha,beta =",alpha,beta)
    tr = (3 * alpha + beta * b) / p
    M_2_2 = (3*alpha*alpha + beta*beta*a*c + 2*alpha*beta*b)/(p*p)
    det = (alpha * alpha * alpha + alpha * alpha * beta * b + beta * beta * beta * a * a * d + alpha * beta * beta * a * c) / (p * p * p)

    updated_a = 1
    updated_b = -2 * tr
    updated_c = (tr * tr) + M_2_2
    updated_d = det - tr * M_2_2

    print("[",updated_a,",",updated_b,",",updated_c,",",updated_d,"],")
    #print("tr,M_2_2,det", tr,M_2_2,det)

    condition_1 = updated_b
    condition_2 = updated_b * updated_b - 3 * updated_a * updated_c
    condition_3 = 27 * updated_a * updated_a * updated_d - 9 * updated_a * updated_b * updated_c + 2 * updated_b * updated_b * updated_b

    #print("Conditions for the case when (a,b,c,d,alpha,beta) = ", a,b,c,d,alpha,beta)
    #ignoring negative sign
    condition_1_factorization = prime_factors(int(abs(condition_1)))
    condition_2_factorization = prime_factors(int(abs(condition_2)))
    condition_3_factorization = prime_factors(int(abs(condition_3)))

   # print("condition_1: ", condition_1, "      ", condition_1_factorization)
   # print("condition_2: ", condition_2, "      ", condition_2_factorization)
    #print("condition_3: ", condition_3, "      ", condition_3_factorization)

    possible_extension = False

    condition_1_factorization = set(condition_1_factorization)
    condition_2_factorization = set(condition_2_factorization)
    condition_3_factorization = set(condition_3_factorization)

    for prime in condition_2_factorization:
        if prime == 0 or prime == 3: continue
        if prime in condition_1_factorization: continue
        if int(condition_2)%(prime*prime) == 0 and int(condition_3)%(prime*prime*prime) == 0:
            possible_extension = True
            print("Possible extension with p =", prime)
            #print("Case when a,b,c,d =", a,b,c,d)
            print("[", updated_a, ",", updated_b, ",", updated_c, ",", updated_d, "],")
            print()

    if not possible_extension:
        pass
        #print("Not possible to extend")

    #print("extra case for p = 3")
    #possible_extend_to_3(updated_a,updated_b,updated_c,updated_d)
    #print("-----")

    # look for prime factors for condition_2 and condition_3



possible_a_b_c_d = [
    [1 , 1, 3, 3]
]

'''
for b in range(0,64,2):
    for c in range(0,64):
        for d in range(0,64):
            if not discriminant_is_zero(4,b,c,d):
                possible_a_b_c_d.append([4,b,c,d])
                '''

print(len(possible_a_b_c_d))

possible_alpha_beta = [
    [1,1]
]

p = 2

check_for_extension(1,1,3,3,1,1,2)

for possibility in possible_a_b_c_d:
    a,b,c,d = possibility[0],possibility[1],possibility[2],possibility[3]
    discriminant = b * b * c * c - 4 * c * c * c * a - 4 * b * b * b * d + 18 * a * b * c * d - 27 * a * a * d * d
    if discriminant == 0:
        print("this is not a ring for", a,b,c,d)
        continue
    for possibility2 in possible_alpha_beta:
        alpha,beta = possibility2[0],possibility2[1]
        #print(a,b,c,d,alpha,beta)

        check_for_extension(a,b,c,d,alpha,beta,p)
                
                '''