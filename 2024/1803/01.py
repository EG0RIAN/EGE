def foo(x):
    s = ""
    while x > 0:
        s = str(x % 4) + s
        x = x // 4
    return s


for x in range(4, 10000):
    s = foo(x)
    if x % 4 == 0:
        s = s + foo(x)[-2::]
    else:
        s = s + foo((x % 4)*2)
    if int(s, 4) < 261:
        print(x)
