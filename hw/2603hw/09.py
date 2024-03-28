from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n <= 2:
        return (n - 1)
    if n > 2:
        return (3 * foo(n - 1)) - foo(n - 2)


# for i in range(2024):
#     foo(i)

print(foo(6))
