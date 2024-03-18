from itertools import product

nechet_digits = "1357"
chet_digits = "02468"
counter = 0
for x in product(chet_digits, nechet_digits, chet_digits, nechet_digits, chet_digits, nechet_digits, chet_digits, nechet_digits, chet_digits, nechet_digits, chet_digits):
    digit_str = "".join(x)
    zeroes = digit_str.count("0")
    if ((zeroes == 0) and (digit_str.count("1") <= 4) and (digit_str.count("2") <= 4) and (digit_str.count("3") <= 4)  and (digit_str.count("4") <= 4)  and (digit_str.count("5") <= 4) and (digit_str.count("6") <= 4) and (digit_str.count("7") <= 4) and (digit_str.count("8") <= 4) and (digit_str.count("9") <= 4)):
        counter += 1

print(counter)
