def foo(n):
    n = bin(n)[2::]
    if len(n) % 2 == 0:
        kolvo = len(n)
        first_part = n[:kolvo//2:]
        second_part = n[kolvo//2::]
        return int(first_part + "111" + second_part, 2)
    if len(n) % 2 != 0:
        return int("11" + str(n)[2::] + "1", 2)


setik = set()
for x in range(10000):
    result = foo(x)
    if result > 4000:
        setik.add(x)


print(min(setik))
