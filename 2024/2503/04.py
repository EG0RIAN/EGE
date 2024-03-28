from functools import lru_cache


@lru_cache(None)
def foo(n):
    if n >= 1000:
        return 1000
    if (n < 1000) and (n % 2 != 0):
        return n * foo(n + 1)
    if (n < 1000) and (n % 2 == 0):
        return n * (foo(n+1)//2)


for i in range(1001, 1, -1):
    foo(i)

print(foo(998)//foo(1001))
