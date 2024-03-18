file = open("17.txt")

list = [int(x) for x in file]
counter = 0
dvoich = 0
max_summ = 0
min_25_ends = 1000000000

for i in range(len(list)):
    if (abs(list[i]) % 100 == 25):
        min_25_ends = min(min_25_ends, list[i])

for i in range(len(list) - 2):
    dvoich = 0
    if (100 > abs(list[i]) > 9):
        dvoich += 1
    if (100 > abs(list[i+1]) > 9):
        dvoich += 1
    if (100 > abs(list[i+2]) > 9):
        dvoich += 1
    sum_troika = (list[i]+list[i+1]+list[i+2])
    if (dvoich == 1) and (sum_troika < min_25_ends):
        counter += 1
        max_summ = max(max_summ, sum_troika)

print(counter, max_summ)
