# Cryptosystems like RSA works on numbers, but messages are made
# up of characters. How should we convert our messages into 
# numbers so that mathematical operations can be applied?

# The most common way is to take the ordinal bytes of the
# message, convert them into hexadecimal, and concatenate.
# This can be interpreted as a base-16 number, and also represented in base-10.

# To illustrate:
# 	message: HELLO
#	ascii bytes: [72, 69, 76, 76, 79]
#	hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
#	base-16: 0x48454c4c4f
#	base-10: 310400273487

# Convert the following integer back into a message:

int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
hex = hex(int)
bytes = bytearray.fromhex(hex[2:])
message = ""
for b in bytes:	message += chr(b)
print(message)
