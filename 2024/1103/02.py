print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not(y <= x)) or (y == w) or z
                if F == 0:
                    print(w, x, y, z)
