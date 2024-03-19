def foo(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s


for n in range(3, 10000):
    s = foo(n)
    if n % 3 == 0:
        s = s + s[-3::]
    else:
        s = s + foo((n % 3)*3)
    if int(s, 3) > 150:
        print(n)
        break