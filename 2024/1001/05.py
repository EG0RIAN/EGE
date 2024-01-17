def foo(N):
    s = bin(N)[2::]
    last_digit = s[-1]
    s += last_digit
    summa = s.count("1")
    s += str(summa % 2)
    return (int(s, 2))


for s in range(100):
    if foo(s) > 105:
        print(foo(s))
        break
