print("x y z w")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = (z != x) <= ((w <= not(y)) and (y <= x))
                if f == True:
                    print(x, y , z, w)
                print("----------------")
                if f == False:
                    print(x, y , z, w)