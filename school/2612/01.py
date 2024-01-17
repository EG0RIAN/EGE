from sys import setrecursionlimit

setrecursionlimit(10**9)

def foo(x, k):
    if x == 3 and k >= 34:
        return True
    if x == 3 and k < 34:
        return False
    if x < 3 and k > 34:
        return False
    else:
        if x % 2 == 0:
            return foo(x + 1, k + 1) or foo(x + 1, k + 2) or foo(x + 1, k * 2)
        else:
            return foo(x + 1, k + 1) and foo(x + 1, k + 2) and foo(x + 1, k * 2)


for x in range(1, 33):
    if foo(1, x):
        print(x)
        break
