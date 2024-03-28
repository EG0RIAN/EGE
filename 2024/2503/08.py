def foo(n):
    if n < 3:
        return 1
    if n > 2:
        return sum(foo(i) for i in range(1, n))


print(foo(18))
