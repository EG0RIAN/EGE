print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not(y <= (x == w))) and (z <= x)
                if F == True:
                    print(w, x, y, z, F)