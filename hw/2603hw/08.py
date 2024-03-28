from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n > 3:
        return (foo(n - 3)) * n


# for i in range(2024):
#     foo(i)

print(foo(10))
