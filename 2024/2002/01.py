from itertools import permutations

counter = 0
for i in permutations("01234567", 5):
    all_digits = ''.join(i)
    odnerki = all_digits.count("1")
    chet = all_digits
    for i in "0246":
        chet = chet.replace(i, "*")
    nechet = all_digits
    for i in "1357":
        nechet = nechet.replace(i, "*")
    if (odnerki < 1) and (all_digits[0] != "0") and (chet.count("**") == 0) and (nechet.count("**") == 0):
        counter += 1

print(counter)
