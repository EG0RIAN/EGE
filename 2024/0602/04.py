x = 3 * (4 ** 38) + 2 * (4 ** 23) + (4 ** 20) + 3*(4 ** 5) + 2*(4 ** 4) + 1
s = ''
counter = 0
while x != 0:
    if x % 16 == 0:
        print(x)
        counter += 1
    x //= 16

print(counter)
