from itertools import product

setik = 0

for x in product("01234567", repeat=11):
    all_digits = "".join(x)
    for i in "1357":
        all_digits = all_digits.replace(i, "*")
    if (all_digits[0] != "0") and (all_digits.count("*") == 3) and (all_digits.count("**") == 0):
        setik += 1

print(setik)
