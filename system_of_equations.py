from decimal import *

# system of equations that defines whether there's a further extension

#system of equations when only one basis is changed
def solve_system_of_equations(a,b,c,d,alpha,beta, p):
    equation_1 = a * d - beta * a * c - alpha * beta * a
    equation_2 = alpha + beta * b - beta * beta * a
    equation_3 = c + beta * beta * a + 2 * alpha
    equation_4 = beta * beta * b + d - beta * c - beta * beta * beta * a
    equation_5 = -alpha * alpha - beta * beta * a * c - b * d + 2 * a * d * beta - alpha * c - alpha * beta * beta * a
    return equation_1 % p == 0 and equation_2 % p == 0 and equation_3 % p == 0 and equation_4 % (p*p) == 0 and equation_5 % (p*p) == 0

#system of equations when two basis elements are changed
def solve_system_of_equations_2(a,b,c,d,alpha,beta,gamma,p):
    equation_1 = 3*alpha + beta*b + gamma*c
    equation_2 = -a*a*beta*beta*d + 3*alpha*alpha + a*b*beta*d*gamma + a*beta*beta*c - 2*a*beta*d*gamma + 2*alpha*b*beta + b*beta*c*gamma + b*d*gamma*gamma + 2*alpha*c*gamma
    equation_3 = alpha*alpha*alpha + a*a*beta*beta*beta*d - a*b*beta*beta*gamma*d - gamma*a*b*beta*beta*d + a*beta*beta*c*c*gamma + a*alpha*beta*beta*c - 2*a*beta*c*gamma*gamma*d + gamma*gamma*gamma*a*d*d - 3*a*alpha*beta*gamma*d + gamma*gamma*b*b*beta*d + alpha*alpha*b*beta + alpha*b*beta*c*gamma + gamma*gamma*alpha*b*d + alpha*alpha*c*gamma

    if (gamma*beta*beta*b + gamma*gamma*gamma*d - beta*beta*beta*a - beta*gamma*gamma*c) == 0:
        return False

    zeta_for_omega_1 = Decimal((gamma*p*p)/(gamma*beta*beta*b + gamma*gamma*gamma*d - beta*beta*beta*a - beta*gamma*gamma*c))
    eta_for_omega_1 = Decimal((-p*(beta*beta*a+gamma*gamma*c+2*alpha*gamma))/(gamma*beta*beta*b + gamma*gamma*gamma*d - beta*beta*beta*a - beta*gamma*gamma*c))
    xi_for_omega_1 = Decimal((gamma*beta*beta*a*c + gamma*gamma*gamma*b*d - 2*beta*gamma*gamma*a*d + alpha*beta*beta*a + alpha*gamma*gamma*c + alpha*alpha*gamma)/(gamma*beta*beta*b + gamma*gamma*gamma*d - beta*beta*beta*a - beta*gamma*gamma*c))

    are_coefficients_for_omega_1_integers = zeta_for_omega_1.as_integer_ratio()[1] == 1 and eta_for_omega_1.as_integer_ratio()[1] == 1 and xi_for_omega_1.as_integer_ratio()[1] == 1

    zeta_for_omega_2 = Decimal((-beta * p * p) / (
                gamma * beta * beta * b + gamma * gamma * gamma * d - beta * beta * beta * a - beta * gamma * gamma * c))
    eta_for_omega_2 = Decimal((p*(beta*beta*b+gamma*gamma*d+2*alpha*beta))/(gamma * beta * beta * b + gamma * gamma * gamma * d - beta * beta * beta * a - beta * gamma * gamma * c))
    xi_for_omega_2 = Decimal((-beta*beta*beta*a*c - beta*gamma*gamma*b*d + 2*beta*beta*gamma*a*d - alpha*beta*beta*b - alpha*gamma*gamma*d - alpha*alpha*beta)/(gamma * beta * beta * b + gamma * gamma * gamma * d - beta * beta * beta * a - beta * gamma * gamma * c))

    are_coefficients_for_omega_2_integers = zeta_for_omega_2.as_integer_ratio()[1] == 1 and eta_for_omega_2.as_integer_ratio()[1] == 1 and xi_for_omega_2.as_integer_ratio()[1] == 1

    return equation_1 % p == 0 and equation_2 % (p*p) == 0 and equation_3 % (p*p*p) == 0 and are_coefficients_for_omega_1_integers and are_coefficients_for_omega_2_integers