# RSA encryption is modular exponentiation of a message with an exponent e and a modulus N which is normally
# a product of two primes: N = p * q.
#
# Together the exponent and modulus for man RSA "public key" (N, e).
# The most common value for e is 0x10001 or 65537.
#
# "Encrypt" the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23.
# What number do you get as the ciphertext?

e = 65537
p, q = 17, 23
n = p * q

print(pow(12,e,n))