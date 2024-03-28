digit = (5**2022) - (2 * (5**1010)) + (25**850) + 2500
k = ""
while digit != 0:
    k = str(digit % 5) + k
    digit = (digit // 5)
print(k.count("4"))
