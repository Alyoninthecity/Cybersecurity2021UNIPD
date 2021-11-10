"""
shiftASCII(string, n)
function -> ROTn(string, n)
@params -> string
@params -> n -> int value to shift from the ASCII
"""


def shiftASCII(string, n):
    r = ""
    for i in string:
        r += str(chr((ord(i) + n) % 127))
    return r


"""
function -> ROTn(string, n)
@params -> string
@params -> n -> int value to shift from the alphabet
"""


def ROTn(string, n):
    r = ""
    for i in string:
        p = ord(i)
        if i.islower():
            if p > (122 - n):
                r += chr(96 + ((p + n) % 122))
            else:
                r += chr(p + n)
        elif i.isupper():
            if p > (90 - n):
                r += chr(64 + ((p + n) % 90))
            else:
                r += chr(p + n)
        else:
            r += i

    return r
