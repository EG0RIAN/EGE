file = open("17_4.txt")

file_list = [int(x) for x in file]
min_in_file = 0
counter = 0
max_sqr = -10000

for i in range(len(file_list)-1):
    if (file_list[i] % 10 == 5):
        min_in_file = min(min_in_file, min(file_list[i], file_list[i+1]))

sqr_min_in_file = min_in_file ** 2

for i in range(len(file_list)-1):
    min_element = min(file_list[i], file_list[i+1])
    if (min_element % 10 == 5) and ((file_list[i]**2 + file_list[i+1]**2) < sqr_min_in_file):
        counter += 1
        max_sqr = max(max_sqr, (file_list[i]**2 + file_list[i+1]**2))

print(counter, max_sqr)
