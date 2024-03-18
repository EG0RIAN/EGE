def foo(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    return foo(x - 1, y) + foo(x // 2, y)


print(foo(78, 16) * foo(16, 4))
