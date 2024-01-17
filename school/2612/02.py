from sys import setrecursionlimit

setrecursionlimit(10**9)


def foo(kuch1, kuch2, hod):
    if hod == 3 and kuch1 + kuch2 >= 77:
        return True
    if hod < 3 and kuch1 + kuch2 >= 77:
        return False
    if hod == 3 and kuch1 + kuch2 < 77:
        return False
    else:
        if hod % 2 == 0:
            return foo(kuch1 + 1, kuch2, hod+1) or foo(kuch1, kuch2+1, hod+1) or foo(kuch1 * 2, kuch2, hod+1) or foo(kuch1, kuch2 * 2, hod+1)
        else:
            return foo(kuch1 + 1, kuch2, hod+1) or foo(kuch1, kuch2+1, hod+1) or foo(kuch1 * 2, kuch2, hod+1) or foo(kuch1, kuch2 * 2, hod+1)

for x in range(1, 70):
    if foo(7, x, 1):
        print(x)
        break
