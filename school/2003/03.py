def foo(n):
    s = str(bin(n)[2::])
    if n % 2 == 0:
        s += s[-2::]
    else:
        s = "1" + s + "0"
    return int(s, 2)


maxim = set()

for x in range(10000):
    if foo(x) < 100:
        maxim.add(x)

print(max(maxim))
