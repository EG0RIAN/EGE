for x in "0123456789A":
    summa = int(f"982{x}8", 11) + int(f"194{x}7", 11)
    if summa % 58 == 0:
        print(summa // 58)