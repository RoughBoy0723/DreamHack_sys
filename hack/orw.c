__asm__(
	".global run_sh\n"
	"run_sh:\n"
	
	"push 0x67\n"
	"mov rax, 0x32656567756265642f6b6361682f796f626867756f722f656d6f682f\n"
	"push rax\n"
	"mov rdi, rsp\n"
	"xor rsi, rsi\n"
	"xor rdx, rdx\n"
	"mov rax, 2\n"
	"syscall\n"
	"\n"
	"mov rdi, rax\n"
	"mov rsi, rsp\n"
	"sub rsi, 0x30\n"
	"mov rdx, 0x30\n"
	"mov rax, 0x0\n"
	"syscall\n"
	"\n"
	"mov rdi, 1\n"
	"mov rax, 0x1\n"
	"syscall\n"
	"\n"
	"xor rdi, rdi\n"
	"mov rax, 0x3c\n"
	"syscall\n");
void run_sh();

int main() { run_sh(); }
