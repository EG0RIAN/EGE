setik = set()
for A in range(1000, 1, -1):
    for x in range(300):
        for y in range(300):
                logiс_exp = (x < 4) or (x >= 20) or (y >= 3*x + A) or (y < 100)
                if logiс_exp == 1:
                    print((A))
