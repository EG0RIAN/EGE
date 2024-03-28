from functools import lru_cache


@lru_cache(maxsize=None)
def foo(n):
    if n < 3:
        return 2
    if (n > 2) and (n % 2 == 0):
        return (2 * foo(n - 2)) - foo(n - 1) + 2
    if (n > 2) and (n % 2 != 0):
        return (2 * foo(n - 1)) + foo(n - 2) - 2


print(foo(170))
