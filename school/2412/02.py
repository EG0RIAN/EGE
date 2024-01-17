def foo(x, h):
    if x >= 40 and h == 3:
        return True
    elif h == 3 and h < 40:
        return False
    elif h >= 40 and h < 3:
        return True
    else:
        if h % 2 == 0:
            return foo(x + 1, h + 1) or foo(x + 2, h + 1) or foo(x * 2, h + 1)
        else:
            return foo(
                x + 1, h + 1) and foo(x + 2, h + 1) and foo(x * 2, h + 1)


for x in range(1, 62):
    if foo(x, 1):
        print(x)
        break
