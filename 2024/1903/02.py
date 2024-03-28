def foo(n):
    ostatok = bin(n - (n % 4))[2::]
    digit_sum = 0
    for x in str(ostatok):
        digit_sum += int(x)
    ostatok = ostatok + str(digit_sum % 2)
    digit_sum = 0
    for x in str(ostatok):
        digit_sum += int(x)
    ostatok = ostatok + str(digit_sum % 2)
    return int(ostatok, 2)

maxim = set()
for x in range(1000):
    result = foo(x)
    if result > 100:
        maxim.add(result)

print(min(maxim))
