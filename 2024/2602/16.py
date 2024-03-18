from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n == 1:
        return 5
    if n > 1:
        return 2 * n + 1 + foo(n - 1)


print(foo(2024) - foo(2022))
