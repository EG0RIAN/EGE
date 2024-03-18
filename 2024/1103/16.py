from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n == 1:
        return 3
    if n > 1:
        return (3 * n) + (2 * foo(n - 1))


print(foo(2024) - (4 * foo(2022)))
