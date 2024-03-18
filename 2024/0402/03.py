def foo(x, y):
    if (x == 5) or (x == 10):
        return 0
    if x == y:
        return 1
    if x > y:
        return 0
    return foo(x + 1, y) + foo(x * 2, y) + foo(x + 3, y)


print(foo(2, 14))
