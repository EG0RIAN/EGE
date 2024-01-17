def foo(x, h):
    if h == 3 and x >= 29:
        return True
    elif h == 3 and x < 29:
        return False
    elif h < 3 and x >= 29:
        return False
    else:
        if h % 2 == 0:
            return foo(x + 1, h + 1) or foo(x * 2, h + 1)
        else:
            return foo(x + 1, h + 1) and foo(x * 2, h + 1)


for x in range(1, 29):
    if foo(x, 1):
        print(x)
        break
