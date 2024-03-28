from functools import lru_cache


@lru_cache(None)
def foo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (n * (n - 1)) + foo(n - 1) + foo(n - 2)


for i in range(1, 2024):
    foo(i)

print(foo(2024) - foo(2022) - (2 * foo(2021)) - foo(2020))
