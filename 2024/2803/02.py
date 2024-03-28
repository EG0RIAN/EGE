print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not(w <= x)) or ((not(z)) <= (not(y))) or z
                if f == 0:
                    print(y, z, x, w)