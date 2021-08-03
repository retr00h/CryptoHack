# I've encrypted the flag with my secret key, you'll never be able to guess it.

from threading import Thread, Lock
from datetime import datetime
from pwn import xor

encryptedFlag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encryptedFlagBytes = bytes.fromhex(encryptedFlag)

flagFormat = b'crypto{'
keybytes = list()
for i in range(len(flagFormat)):
	keybytes.append(xor(flagFormat[i], encryptedFlagBytes[i]))
keybytes.append(b'y')

decryptedFlagBytes = xor(encryptedFlagBytes, keybytes)
decryptedFlag = ""
for b in decryptedFlagBytes:
	decryptedFlag += chr(b)

print(decryptedFlag)
