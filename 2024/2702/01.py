file = open(file="01.txt")
listik = [int(x) for x in file]
five_digits_per_number_counter = 0
max_digit = -100000000
counter = 0
max_troiki_sum = -100000000
for i in range(len(listik)):
    if (abs(listik[i]) % 1000 == 321):
        max_digit = max(listik[i], max_digit)

for i in range(len(listik) - 2):
    five_digits_per_number_counter = 0
    if (9999 < abs(listik[i]) < 100000):
        five_digits_per_number_counter += 1
    if (9999 < abs(listik[i+1]) < 100000):
        five_digits_per_number_counter += 1
    if (9999 < abs(listik[i+2]) < 100000):
        five_digits_per_number_counter += 1
    troiki_sum = listik[i]+listik[i+1]+listik[i+2]
    if (five_digits_per_number_counter == 2) and ((listik[i] % 5 == 0) or (listik[i+1] % 5 == 0) or (listik[i+2] % 5 == 0)) and (troiki_sum > max_digit):
        max_troiki_sum = max(max_troiki_sum, troiki_sum)
        counter += 1
print(counter, max_troiki_sum)
