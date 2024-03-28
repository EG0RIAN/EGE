def convert(x):
    s = ""
    while x != 0:
        s = str(x % 4) + s
        x = x // 4
    return s


def foo(n):
    s = convert(n)
    if n % 4 == 0:
        s = s + s[-2::]
    if n % 4 != 0:
        s += convert((n % 4) * 2)
    return int(s, 4)

minim = set()

for x in range(4, 10000):
    if foo(x) > 1025:
        minim.add(x)

print(min(minim))