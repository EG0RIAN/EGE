s = (9*11) * (3 ** 20) - (3**9) - 27

x = ''

while s != 0:
    x += str(s%3)
    s //= 2

x=x[::-1]
print(x)

print(x.count("2"))