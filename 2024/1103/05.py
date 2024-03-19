def foo(n):
    s = ""
    k = n
    while k != 0:
        s = str(k % 4) + s
        k = k // 4
    return s


for n in range(4, 1000):
    s = foo(n)

    if n % 4 == 0:
        s += foo(n)[-2::]
    else:
        s += foo((n % 4) * 2)

    if int(s, 4) < 369:
        print(n)
