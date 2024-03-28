def foo(n):
    digit = bin((n - (n % 8)) + (n % 2))[2::]
    summ = 0
    for x in str(digit):
        summ += int(x)
    digit = f"{digit}" + f"{(summ % 2)}"
    for x in str(digit):
        summ += int(x)
    digit = f"{digit}" + f"{(summ % 2)}"
    return int(digit, 2)


maxim = set()
for x in range(10000):
    result = foo(x)
    if result > 90:
        maxim.add(result)

print(min(maxim))