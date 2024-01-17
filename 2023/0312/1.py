def foo(n):
    if n == 0:
        return 0
    if n % 2 == 0 and n > 0:
        return foo(n//2)
    if n % 2 != 0:
        return 1 + foo(n - 1)


k = 0
for n in range(1, 501):
    if foo(n) == 8:
        k += 1

print(k)
