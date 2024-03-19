def foo(n):
    s = str(bin(n)[2::])
    rev_s = ''.join(reversed(s.rstrip('0')))
    return int(rev_s, 2)

for x in range(1, 100):
    if foo(x) == 13:
        print(x)

# Ответ: 88
