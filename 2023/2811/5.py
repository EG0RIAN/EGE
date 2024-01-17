import sys
sys.setrecursionlimit(10**6)


def foo(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + foo(n-1)


print(foo(2124) - foo(2122))
