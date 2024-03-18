from itertools import product

chet = "02468"
nechet = "1357"
counter = 0
for x in product(nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet):
    digit_str = "".join(x)
    zeroes = digit_str.count("0")
    if (zeroes == 0) and (digit_str.count("1") <= 3) and (digit_str.count("2") <= 3) and (digit_str.count("3") <= 3)  and (digit_str.count("4") <= 3)  and (digit_str.count("5") <= 3) and (digit_str.count("6") <= 3) and (digit_str.count("7") <= 3) and (digit_str.count("8") <= 3):
        counter += 1

print(counter)
