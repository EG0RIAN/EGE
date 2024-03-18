for a in range(100, 0, -1):
    k = True
    for x in range(1, 1000):
        f = (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))
        if f == False:
            k = False
    if k == True:
        print(a)
        break