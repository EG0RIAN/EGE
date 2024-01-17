def foo(n):
    if n == 1:
        return 2
    elif n >= 2:
        return foo(n - 1) * n


print(foo(5))
