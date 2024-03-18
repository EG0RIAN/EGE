def foo(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return foo(x + 1, y) + foo(x + 3, y)


print(foo(2, 15))
