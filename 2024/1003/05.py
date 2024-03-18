for x in "0123456789ABCD":
    digit = int(f"3D4{x}", 16) + int(f"4{x}C4", 14)
    if digit % 154 == 0:
        print(digit//154)
        break
