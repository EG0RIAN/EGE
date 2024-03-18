def foo(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x == 11:
        return 0
    return foo(x + 1, y) + foo(x + 4, y) + foo(x * 2, y)

print(foo(4, 11) + foo(11, 28))