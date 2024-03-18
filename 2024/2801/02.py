file = open("17_2.txt")
list = [int(x) for x in file]
counter = 0
maxm = -10000
for i in range(len(list) - 1):
    for j in range(i + 1, len(list)):
        if ((list[i] + list[j]) % 60 == 0) and ((list[i] % 40 == 0) or (list[j] % 40 == 0)):
            counter += 1
            maxm = max(maxm, list[i] + list[j])

print(counter, maxm)
