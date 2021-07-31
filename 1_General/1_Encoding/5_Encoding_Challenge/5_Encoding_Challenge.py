# Now you've got the hang of the various encodings you'll
# be encountering, let's have a look at automating it.
# Can you pass all 100 levels to get the flag?

# The 13377.py file attached below is the source code for
# what's running on the server.
# The pwntools_example.py file provides the start of a
# solution using the incredibly convenient pwntools library.
# which you can use if you like.
# pwntools however is incompatible with Windows,
# so telnetlib_example.py is also provided.

# Connect at "nc socket.cryptohack.org 13377"

from pwn import * # pip install pwntools
from Crypto.Util.number import long_to_bytes
import json
import sys

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def print_msg(i, msg = "Sent!"):
	if msg == "Sent!": print(str(i) + " - " + msg)
	else: print(str(i) + " - Decoded message: " + str(msg) + "\nSending...")

def decode_rot13(encoded):
	message = ""
	for c in encoded:
		if c == '_': message += c
		else:
			newC = chr(ord(c) - 13)
			if newC < 'a': newC = chr(ord(newC) + 26)
			elif newC > 'z': newC = chr(ord(newC) - 26)
			message += newC
	return message

r = remote('socket.cryptohack.org', 13377)
i = 0
while True:
	received = json_recv()
	if "error" in received.keys():
		print("ERROR: DECODING FAILED :(")
		sys.exit()
	elif "flag" in received.keys():
		print("FLAG: " + received["flag"])
		sys.exit()
	elif received["type"] == "utf-8":
		print(str(i) + " - Type received: " + received["type"])
		encoded = received["encoded"]
		msg = ""
		for c in encoded:
			msg += str(int(c))
		print(str(i) + " - Encoded message received: " + msg)
		message = ""
		for b in encoded:
			message += chr(b)
		print_msg(i, message)
		json_send({"decoded": message})
		print_msg(i)
	else:
		print(str(i) + " - Type received: " + received["type"])
		print(str(i) + " - Encoded message received: " + received["encoded"])
		if received["type"] == "base64":
			message = str(base64.b64decode(received["encoded"]))
			print_msg(i, message[1:])
			json_send({"decoded": message[2:len(message)-1]})
			print_msg(i)
		elif received["type"] == "hex":
			hex = received["encoded"]
			bytes = bytearray.fromhex(hex)
			message = ""
			for b in bytes:
				message += chr(b)
			print_msg(i, message)
			json_send({"decoded": message})
			print_msg(i)
		elif received["type"] == "rot13":
			message = decode_rot13(received["encoded"])
			print_msg(i, message)
			json_send({"decoded": message})
			print_msg(i)
		elif received["type"] == "bigint":
			# int = int(received["encoded"], 16)
			# hex = int.to_bytes(0, "big")
			bytes = bytearray.fromhex(received["encoded"][2:])
			message = ""
			for b in bytes:
				message += chr(b)
			print_msg(i, message)
			json_send({"decoded": message})
			print_msg(i)
	i += 1
