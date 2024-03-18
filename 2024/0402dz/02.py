print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not((not(y) or z))) or (x == w) or x
                if F == 0:
                    print(w, x, y, z, F)
