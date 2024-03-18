setik = set()
for x in "012345678":
    for y in "012345678":
        digit = int(f"2{y}66{x}", 9) + int(f"{x}0{y}1", 12)
        if digit % 170 == 0:
            setik.add(digit//170)

print(min(setik))
