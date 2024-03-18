setik = set()
for x in "0123456789AB":
    for y in "0123456789AB":
        digit = int(f"{x}231{y}", 12) + int(f"78{x}98{y}", 14)
        if digit % 99 == 0:
            setik.add(digit//99)

print(min(setik))
