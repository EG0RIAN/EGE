for A in range(0, 10000):
    flag = True
    for x in range(1, 1000):
        f = (x & 33 == 0) >= ((x & 45 != 0) >= (x& A != 0))
        if f == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
