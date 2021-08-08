# We'll pick up from the last challenge and imagine we've
# picked a modulus p, and we will restrict ourselves to the case when p is prime.

# The integers modulo p define a field, denoted Fp.

#	If the modulus is not prime, the set of integers modulo n define a ring.

# A finite field Fp is the set of integers {0,1,...,p-1},
# and under both addition and multiplication there is an inverse element
# b for every element a in the set, such that a + b = 0 and a * b = 1.

#	A field is a general name for a commutative ring in which
#	every non-zero element has a multiplicative inverse.

#	Note that the identity element for addition and multiplication is different!
#	This is because the identity when acted with the operator should do
#	nothing: a + 0 = a and a * 1 = a.

# Lets say we pick p = 17. Calculate 3^(17) mod 17.
# Now do the same but with 5(17) mod 17.

p = 17
m1 = 3**17 % p
m2 = 5**17 % p
print(m1, m2)

# What would you expect to get for 7^(16) mod 17? Try calculating that.

m3 = 7**(p-1) % p
print(m3)

# This interesting fact is known as Fermat's little theorem.
# We'll be needing this (and its generalisations) when we look at RSA cryptography.

# Now take the prime p = 65537. Calculate 273246787654^(65536) mod 65537.

p = 65537
m = 273246787654**(p-1) % p
print(m)
