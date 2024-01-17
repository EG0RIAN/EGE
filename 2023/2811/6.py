import sys
sys.setrecursionlimit(10**6)


def foo(n):
    if n < 1000:
        if n % 2 != 0:
            return n * foo(n + 1)
        else:
            return n * (foo(n + 1)//2)

    return 1000


print(foo(998)//foo(1001))
