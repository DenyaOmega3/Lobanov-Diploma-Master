def compute_discriminant(a,b,c,d):
    discriminant = b * b * c * c - 4 * c * c * c * a - 4 * b * b * b * d + 18 * a * b * c * d - 27 * a * a * d * d
    return discriminant

def discriminant_is_zero(a,b,c,d):
    discriminant = compute_discriminant(a,b,c,d)
    return discriminant == 0