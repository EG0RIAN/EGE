for a in range(200, 0, -1):
    k = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = ((x <= 9) <= ((x * x) <= a)) and (((y * y) <= a) <= (y <= 9))
            if f == False:
                k = False
    if k == True:
        print(a)
        break