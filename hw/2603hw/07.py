from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n * foo(n + 1)


for i in range(2024):
    foo(i)

print(foo(2022)//foo(2024))
