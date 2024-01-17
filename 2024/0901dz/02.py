print("w x y z F")

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if y and (x or z) or not (y or z) or w == 0:
                    print(w, x, y, z)
