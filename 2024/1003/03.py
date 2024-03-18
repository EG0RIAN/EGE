for x in "0123456789ABCDEFGHI":
    digit = int(f"78{x}79643", 19) + int(f"25{x}43", 19) + int(f"63{x}5", 19)
    if digit % 18 == 0:
        print(digit // 18)
        break