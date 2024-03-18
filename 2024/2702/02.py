def foo(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + foo(2*n)


def goo(n):
    return foo(n) // n


vdv = goo(2000)

counter = 0
for x in range(1, 1000000):
    if goo(x) == vdv:
        counter += 1

print(counter)
