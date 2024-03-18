for a in range(100, 0, -1):
    k = True
    for x in range(1, 1000):
        f = (x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))
        if f == False:
            k = False
    if k == True:
        print(a)
        break
