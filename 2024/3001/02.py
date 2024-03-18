print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not(x <= y)) or (x == z) or w
                if F == False:
                    print(w, x, y, z, F)
