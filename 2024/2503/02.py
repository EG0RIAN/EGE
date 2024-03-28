from functools import lru_cache


@lru_cache(None)
def foo(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + foo(n - 1)


for i in range(1, 2021):
    foo(i)

print(foo(2021) - foo(2019))
