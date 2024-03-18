def foo(x, y, z):
    if x == y:
        return 1
    if x > y + 1:
        return 0
    if z == 1:
        return foo(x * 2, y, 2) + foo(x * 3, y, 3)
    return foo(x - 1, y, 1) + foo(x * 2, y, 2) + foo(x * 3, y, 3)


print(foo(3, 15, 0))
