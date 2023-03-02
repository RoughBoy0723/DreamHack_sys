	.file	"cdecl.c"
	.text
	.globl	callee
	.type	callee, @function
callee:
.LFB0:
	.cfi_startproc
	nop
	ret
	.cfi_endproc
.LFE0:
	.size	callee, .-callee
	.globl	caller
	.type	caller, @function
caller:
.LFB1:
	.cfi_startproc
	pushl	$2
	.cfi_def_cfa_offset 8
	pushl	$1
	.cfi_def_cfa_offset 12
	call	callee
	addl	$8, %esp
	.cfi_def_cfa_offset 4
	nop
	ret
	.cfi_endproc
.LFE1:
	.size	caller, .-caller
	.ident	"GCC: (Ubuntu 11.2.0-19ubuntu1) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
