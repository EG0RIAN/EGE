file = open("17_1.txt")

list = [int(x) for x in file]
counter = 0
max_number = 0

for i in range(len(list) - 1):
    if ((list[i]*list[i+1]) % 15 == 0) and ((list[i]+list[i+1]) % 7 == 0):
        counter += 1
        max_number = max(max_number, list[i]+list[i+1])

print(counter, max_number)
