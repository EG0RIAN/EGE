def foo(x, h):
    if h == 3 and x >= 62:
        return True
    elif h == 3 and x < 62:
        return False
    elif h < 3 and x >= 62:
        return False
    else:
        if h % 2 == 0:
            return foo(x + 1, h + 1) + foo(x + 4, h + 1) + foo(x*5, h + 1)
        else:
            return foo(x + 1, h + 1) + foo(x + 4, h + 1) + foo(x*5, h + 1)


for x in range(1, 62):
    if foo(x, 1):
        print(x)
        break
