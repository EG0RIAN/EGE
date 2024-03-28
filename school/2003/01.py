def foo(n):
    s = str(bin(n)[2::])
    if n % 3 == 0:
        s = s + s[-3::]
    else:
        s = s + bin((n % 3) * 3)[2::]
    return int(s, 2)


minim = set()

for x in range(10000):
    result = foo(x)
    if result > 151:
        minim.add(result)
print(min(minim))
