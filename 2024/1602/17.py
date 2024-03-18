file = open("17.txt")

list = [int(x) for x in file]
counter = 0
min_number = min(list)
min_sum = 1000000

for i in range(len(list) - 1):
    if ((list[i] % 14) + (list[i+1] % 14)) == min_number:
        counter += 1
        min_sum = min(min_sum, (list[i] + list[i+1]))

print(counter, min_sum)
