for x in '0123456789ABC':
    digit = (int(f"26{x}98", 13) + int(f"4{x}296", 13))
    if digit % 34 == 0:
        print(digit//34)
        break
