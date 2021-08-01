# I've hidden my data using XOR with a single byte. Don't forget to decode from hex first.

from pwn import xor


xordString = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

xorbytes = bytes.fromhex(xordString)

for i in range(256):
	possibleFlag = xor(xorbytes, i)
	message = ""
	for c in possibleFlag:
		message += chr(c)
	if "crypto{" in message:
		print(message)
