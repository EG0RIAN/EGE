def convert(n):
    str_to_re = ""
    while n > 0:
        str_to_re = str(n % 3) + str_to_re
        n = n // 3
    return str_to_re


def foo(n):
    s = str(convert(n))
    if len(s) - s.count("1") > s.count("1"):
        s = "22" + s
    else:
        s = "11" + s
    return int(s, 3)


minim = set()
for x in range(11, 1000):
    result = foo(x)
    if result > 100:
        minim.add(result)

print(min(minim))
