for a in range(100, 0, -1):
    k = True
    for x in range(1, 1000):
        f = ((x & 116 != 0) or (x&92 != 0)) <= ((x&69 == 0) <= (x&a != 0))
        if f == False:
            k = False
    if k == True:
        print(a)