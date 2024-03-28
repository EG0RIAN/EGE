for x in "0123456789A":
    for y in "0123456789AB":
        summa = int(f"95{x}2", 11) + int(f"{y}458", 12)
        if summa % 136 == 0:
            print(summa // 136)