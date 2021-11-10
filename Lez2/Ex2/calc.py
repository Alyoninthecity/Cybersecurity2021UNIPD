def cal(a1, b1, o):
    a = int(a1)
    b = int(b1)
    if o == "0":
        print(a + b)
    elif o == "1":
        print(a - b)
    elif o == "2":
        print(a * b)
    elif o == "4":
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Vuoi creare un buco nero?")
    else:
        print("Input non validi")


cal(input("Inserisci a: "), input("\nInserisci b: "), input("\nInserisci c: "))
