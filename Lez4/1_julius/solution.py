import base64
import re


def base64ToString(base64):
    reg = "\\x[a-z0-9][a-z0-9]"
    base64.b64decode()
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")


def shiftASCII(string, n):
    r = ""
    for i in string:
        r += str(chr((ord(i) + n) % 127))
    return r


for i in range(0, 127):
    message = "}{[l^KlwOmwZjmOKW9"
    print(shiftASCII(message, i))
# ecCTF3T_7U_BRU73?!