from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(5_000)


@lru_cache(None)
def foo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (n * (n - 1)) + foo(n - 1) + foo(n - 2)


print(foo(2024) - foo(2022) - (2 * foo(2021)) - foo(2020))
