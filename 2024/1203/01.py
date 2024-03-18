for x in "0123456789ABCDEFGHIJKLM":
    first_digit_s = f"1{x}1{x}1{x}1{x}1"
    second_digit_s = f"20{x}24"
    third_digit_s = f"1{x}235"
    summa = int(first_digit_s, 23) + int(second_digit_s, 23) + int(third_digit_s, 23)
    if summa % 22 == 0:
        print(summa//22)
