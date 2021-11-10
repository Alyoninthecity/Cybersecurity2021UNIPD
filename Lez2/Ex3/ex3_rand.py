from random import randint


def randAlphnum(l):
    c = ord("0")
    r = ""
    for i in range(0, l):
        x = randint(0, 59)
        if x >= 10 and x <= 35:
            r += str(chr(c + x + 7))
        elif x > 35:
            r += str(chr(c + x + 6 + 7))
        else:
            r += str(chr(c + x))
    return r


print(randAlphnum(10))
