def foo(n):
    k = str(bin(n)[2::])
    if n % 3 == 0:
        k = k.replace("0", "11", -1)
    if n % 3 != 0:
        k = k.replace("1", "10", -1)
    return int(k, 2)


max_r = set()

for x in range(1000):
    result = foo(x)
    if result <= 161:
        max_r.add(result)

print(max(max_r))
