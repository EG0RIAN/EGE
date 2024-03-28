import sys

sys.setrecursionlimit(10 ** 4)


def foo(n):
    if n >= 10000:
        return 1
    if n < 10000 and n % 2 == 0:
        return foo(n + 3) + 7
    return foo(n + 1) - 3


print(foo(50) - foo(57))
