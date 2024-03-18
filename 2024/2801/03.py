file = open("17_3.txt")

file_list = [int(x) for x in file]

counter = 0
mmax = -10000
for i in range(len(file_list)-1):
    for j in range(i+1, len(file_list)):
        if ((file_list[i] - file_list[j]) % 80 == 0):
            counter += 1
            mmax = max(mmax, file_list[i] - file_list[j])

print(counter, mmax)
