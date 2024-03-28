def foo(x, h):
    if h == 3 and x >= 40:
        return 1
    if h == 3 and x < 40:
        return 0
    if h >= 3 and x < 40:
        return 0
    else:
        if h % 2 == 0:
            return foo(x + 1, h + 1) or foo(x + 4, h + 1) or foo(x * 2, h + 1)
        else:
            return foo(x + 1, h + 1) and foo(x + 4, h + 1) and foo(x * 5, h + 1)


for x in range(1, 39):
    if foo(x, 1) == 1:
        print(x)
        break
