def foo(x, y):
    if (x > y) or (x == 21):
        return 0
    if x == y:
        return 1
    return foo(x + 2, y) + foo(x + 3, y) + foo(x + 3, y) + foo(x * 5, y)


print(foo(1, 6) + foo(6, 35))

# 45982
