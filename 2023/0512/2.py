for N in range(100):
    s = bin(N)[2:]
    if N % 2 == 0:
        s += "00"
    else:
        s += "11"

    if int(s, 2) > 115:
        print(N)
        break
