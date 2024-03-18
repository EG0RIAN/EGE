def foo(x, y):
    if x == y:
        return 1
    if (x > y) or (x == 11) or (x == 17):
        return 0
    return foo(x + 1, y) + foo(x + 4, y) + foo(x * 2, y)


print(foo(3, 24))
