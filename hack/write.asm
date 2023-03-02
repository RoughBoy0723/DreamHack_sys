section .text
global _start
_start:
	mov rax, 0x676e6f6f6f6f6f6f6c5f73695f656d616e5f67616c662f63697361625f6c6c6568732f656d6f682f
	push rax
	mov rsi, rsp
	push 1
	pop rdi
	push 0x30
	pop rdx
	push 1
	pop rax
	syscall
