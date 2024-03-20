def change_digit(n):
    k = ""
    while n != 0:
        k = str(n % 5) + k
        n = n // 5
    return k


def foo(n):
    if n % 25 == 0:
        r = str(change_digit(n))[-3::] + str(change_digit(n))
    if n % 25 != 0:
        r = str(change_digit(n)) + change_digit(n % 25)
    return int(r, 5)


minik = set()
for x in range(5, 100000):
    if foo(x) > 10000:
        minik.add(x)

print(min(minik))