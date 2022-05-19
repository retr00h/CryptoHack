# RSA relies on the difficulty of the factorisation of the modulus N. If the primes can be found then we can calculate hte Euler totient (https://leimao.github.io/article/RSA-Algorithm/) of N and thus decrypt the ciphertext.
#
# Given N = p * q and two primes:
#
# p = 857504083339712752489993810777
#
# q = 1029224947942998075080348647219
#
# What is the totient of N?

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

print((p-1)*(q-1))