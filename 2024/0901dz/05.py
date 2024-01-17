for N in range(100):
    s = bin(N)[2:]
    if s % 2 == 0:
        s += str(s)[-2:]
    else:
        s = ("1" + s + "0")

    if int(s, 2) <= 100:
        print("Ответ", N)
        break
