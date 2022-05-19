# The privat key d is used to decrypt ciphertext created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).
#
# The private key is the secret piece of information or "trapdoor" which allows us to quickly invert the encryption function.
# If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to first factorise the modulus.
#
# In RSA the private key is the modular multiplicative inverse (https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of the exponent e modulo the totient of N.
#
# Given the tGiven the two primes:
#
# p = 857504083339712752489993810777
#
# q = 1029224947942998075080348647219
#
# and the exponent:
#
# e = 65537
#
# What is the private key d?

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

def gcd(a, b):
  while True:
    if a == b: return a
    elif a > b: a = a - b
    else: b = b - a


eulerTotient = (p - 1) * (q - 1)
N = p * q

for d in range(1, eulerTotient):
  if gcd(d, eulerTotient) == 1:
    print(d)
    break