def convert(x):
    if x == 0:
        return 0

    k = ""
    while x != 0:
        k = str(x % 4) + k
        x = x // 4
    return k

def foo(n):
    chet = convert(n)
    print(chet)
    if (n % 4 == 0):
        n = chet + chet[-2::]
    if (n % 4 != 0):
        print("ad")
    return n

print(foo(12))
