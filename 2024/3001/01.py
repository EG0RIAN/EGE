def foo(n):
    if n < 3:
        return 1
    if (n > 2) and (n % 2 != 0):
        return foo(n - 1) + foo(n - 2)
    if (n > 2) and (n % 2 == 0):
        total = 0
        for i in range(1, n):
            total += foo(i)
        return total


print(foo(24))
