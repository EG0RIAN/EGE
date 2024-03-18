for x in "012345678":
    digit = (int(f"88{x}4{x}"), 9) + int(f"7{x}344", 9)
    if digit % 67 == 0:
        print(digit//67)
