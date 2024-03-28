from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n == 1:
        return 1
    if n > 1:
        return n * foo(n - 1)


print(foo(2023)//foo(2020))
