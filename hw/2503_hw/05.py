def foo(n):
    k = str(bin(n)[2::])
    frstthrrzrds = k[:3:]
    summa = 0
    for x in range(len(str(len(frstthrrzrds)))):
        summa += x
    if summa % 2 == 0:
        k = f"1{k[:-2:]}01"
    if summa % 2 != 0:
        k = f"10{k[2::]}1"
    return int(k, 2)


max_n = set()

for x in range(1000):
    result = foo(x)
    if result > 50:
        max_n.add(x)

print(min(max_n))
