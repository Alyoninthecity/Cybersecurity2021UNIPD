def shift(string):
    for c in string:
        print(chr(ord(c) + 2))


shift(input("Inserisci la stringa: "))