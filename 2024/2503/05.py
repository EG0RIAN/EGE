from functools import lru_cache


@lru_cache(None)
def foo(n):
    if n >= 2000:
        return 2000
    if (n < 2000) and (n % 2 != 0):
        return n * foo(n + 1)
    if (n < 2000) and (n % 2 == 0):
        return n * (foo(n + 1)//2)


for i in range(2000, 1, -1):
    foo(i)

print(foo(1998)//foo(2001))
