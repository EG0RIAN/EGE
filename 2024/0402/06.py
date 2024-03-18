def foo(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return foo(x + 1, y) + foo(x * 3, y) + foo(x + 2, y)

print(foo(2, 9) * foo(9, 11) * foo(11, 12))