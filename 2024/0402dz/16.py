def foo(n):
    if n < 3:
        return 1
    if (n > 2) and (n % 2 == 0):
        return foo(n - 2) - foo(n - 1)
    if (n > 2) and (n % 2 != 0):
        return 2*(foo(n-1)) - foo(n - 2)


print(foo(19))
