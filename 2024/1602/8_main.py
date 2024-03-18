from itertools import product

count = set()

for s in product("01234567", repeat=5):
    digit_str = ''.join(s)
    if (digit_str[0] != "0") and (digit_str.count("6") == 1) and ("16" not in digit_str) and ("61" not in digit_str) and ("36" not in digit_str) and ("63" not in digit_str) and ("56" not in digit_str) and ("65" not in digit_str) and ("76" not in digit_str) and ("67" not in digit_str):
        count.add(digit_str)

print(len(count))
