def foo(n):
    if n == 1:
        return 1
    else:
        return foo(n - 1) + n


print(foo(40))
