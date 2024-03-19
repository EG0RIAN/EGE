for x in range(300):
    for y in range(300):
        for A in range(300):
            f = ((x**2 + y**2) > 128) or (y < (-x + A))
            if f == 1:
                print(A)
                break