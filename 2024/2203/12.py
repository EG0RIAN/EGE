setik = set()
for x in range(100000):
    digit = "4" + "1"*x
    while ("31" in digit) or ("411" in digit) or ("1111" in digit):
        digit = digit.replace("31", "1", 1)
        digit = digit.replace("411", "13", 1)
        digit = digit.replace("1111", "4", 1)
    summa = 0
    for z in digit:
        summa += int(x)
        if summa == 36:
            print(x)

print(min(setik))
