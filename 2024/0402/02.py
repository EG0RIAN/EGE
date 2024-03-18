def foo(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return foo(x + 1, y) + foo(x * 2, y) + foo((2 * x) + 1, y) + foo(x * 10, y)


print(foo(1, 15))
