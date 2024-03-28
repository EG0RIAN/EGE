def convert(n):
    str_to_re = ""
    while n > 0:
        str_to_re = str(n % 6) + str_to_re
        n = n // 6
    return str_to_re


def foo(n):
    s = str(convert(n))
    if n % 3:
        s = s + s[0:2]
    else:
        s = s + convert((n % 3) * 10)
    return int(s, 6)

print(foo(12))

# minim = set()
# for x in range(11, 1000):
#     result = foo(x)
#     if result > 100:
#         minim.add(result)

# print(min(minim))
