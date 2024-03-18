for a in range(100, 0, -1):
    k = True
    for x in range(1, 1000):
        f = ((x % 2 == 0) <= (x % 3 != 0)) or ((x + a) >= 100)
        if f == False:
            k = False
    if k == True:
        print(a)
