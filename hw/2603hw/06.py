from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if (n % 3 == 0) and (n > 0):
        return n + foo(n - 3)
    if n % 3 > 0:
        return n + foo(n - (n % 3))
    return 0


print(foo(26))
