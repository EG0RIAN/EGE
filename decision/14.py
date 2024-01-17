minimum = 10 ** 12
for x in range(9):
    for y in range(9):
        result = (8 * 9 ** 4) + (8 * 9 ** 3) + (x * 9 ** 2) + (4 * 9) + y + (7 * 11 ** 4) + (x * 11 ** 3) + (4 * 11 ** 2) + (4 * 11) + y
        if result % 61 == 0:
            minimum = min(result, minimum)
print(minimum // 61)