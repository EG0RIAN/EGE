from functools import lru_cache


@lru_cache(None)
def foo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (n * (n - 1)) + foo(n - 1) - foo(n - 2)


for x in range(2024):
    foo(x)


print(foo(2024) + foo(2020) - foo(2019))

# 4102638