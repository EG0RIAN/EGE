mx = 0
for n in range(1, 30):
    if n % 3 == 0:
        r = n * 9 + 2
        z = 1
        while z <= r:
            z *= 3
        r += z
    elif n % 3 == 1:
        r = n * 9 + 4
    else:
        r = n * 9 + 8
    if r < 199:
        mx = n
print(mx)

# 20
