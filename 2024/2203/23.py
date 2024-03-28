def foo(x, y):
    if (x > y) or (x == 6) or (x == 17):
        return 0
    if x == y:
        return 1
    return foo(x + 2, y) + foo(x + 3, y) + foo(x * 5, y)


print(foo(1, 31))
