def smth(x, y):
    if x == y:
        return 1
    if x < y or x == 5:
        return 0
    return smth(x-1, y) + smth(x//2, y)


print(smth(45, 15)*smth(15, 3))
