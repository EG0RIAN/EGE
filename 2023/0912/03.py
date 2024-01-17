import sys

sys.setrecursionlimit(10**9)


def foo(n):
    if n < 11:
        return n
    if n >= 11:
        return n + foo(n-1)


print(foo(2024)-foo(2021))
