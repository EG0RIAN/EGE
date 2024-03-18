from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return foo(x - 2, y) + foo(x - 5, y)


print(foo(17, 1))
