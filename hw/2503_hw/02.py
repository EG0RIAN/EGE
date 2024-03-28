def convert(n):
    if n == 0:
        return "0"
    s = ""
    while n != 0:
        s = str(n % 6) + s
        n = n // 6
    return s


def foo(n):
    k = str(convert(n))
    if n % 3 == 0:
        s = str(k) + str(k[:2:])
    if n % 3 != 0:
        s = str(k) + str(convert((n % 3) * 10))
    return int(s, 6)


min_r = set()

for x in range(6, 1000):
    result = foo(x)
    if result > 680:
        min_r.add(result)

print(min(min_r))
