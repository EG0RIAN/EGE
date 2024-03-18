from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n < 15:
        return n
    if n >= 15:
        return n + foo(n - 1)


print(foo(2025) - foo(2022))
