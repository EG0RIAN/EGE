from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n == 1:
        return 1
    if n > 1:
        return (2 * foo(n - 1)) + 1


# for i in range(2024):
#     foo(i)

print(foo(6))
