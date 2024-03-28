def foo(x, h):
    if h == 3 and x >= 63:
        return 1
    elif h == 3 and x < 63:
        return 0
    elif h < 3 and x >= 63:
        return 0
    else:
        if h % 2:
            return foo(x + 1, h + 1) or foo(x + 4, h + 1) or foo(x * 5, h + 1)
        else:
            return foo(x + 1, h + 1) or foo(x + 4, h + 1) or foo(x * 5, h + 1)

for x in range(1, 63):
    if foo(x, 1) == 1:
        print(x)
        break