def foo(n):
    n = bin(n)[2::]
    if int(n,2) % 5 == 0:
        n = n + "101"
        if int(n,2) % 7 == 0:
            n = n + "111"
        else:
            n = n + "1"
    else:
        n = n + "1"
        if int(n,2) % 7 == 0:
            n = n + "111"
        else:
            n = n + "1"
    return int(n,2)


for n in range(1000000, 1 , -1):
    if foo(n) < 1728404:
        print(n)
        break