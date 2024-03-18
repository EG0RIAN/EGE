for x in "0123456789AB":
    digit_one = int(f"2AB{x}", 12) + int(f"{x}8E", 17)
    if digit_one % 27 == 0:
        print(digit_one//27)
        break
