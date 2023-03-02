from pwn import *

def slog(name, addr): 
	return success(": ".join([name, hex(addr)]))

p = remote("host3.dreamhack.games",14258)

p.interactive()
