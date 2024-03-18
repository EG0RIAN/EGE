x = (4 ** 36) + 3 * (4 ** 20) + (4 ** 15) + 2 * (4 ** 7) + 49

counter = 0
unique_digits = set()
while x != 0:
    unique_digits.add(x % 16)
    x //= 16

print(unique_digits)
