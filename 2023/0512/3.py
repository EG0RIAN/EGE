o1 = 0
o2 = 0
q1 = bin(876544)[2:]
q2 = int(q1[:len(q1)-3], 2)
for n in range(q2 - 10, q2 + 10):
    s = bin(n)[2:]
    for i in range(3):
        count1 = 0
        count2 = 0
        l = int(s, 2)
        l1 = l
        while l > 0:
            if (l % 10) % 2 == 0:
                count2 += 1
                l //= 10
            elif (l % 10) % 2 != 0:
                count1 += 1
                l //= 10
        if count2 > count1:
            s += '1'
        elif count2 < count1:
            s += '0'
        elif count1 == count2:
            if l1 % 2 == 0:
                s += '0'
            else:
                s += '1'
    r = int(s, 2)
    if 876544 <= r and r <= 1234567899:
        o1 = n
        break
k1 = bin(1234567899)[2:]
k2 = int(k1[:len(k1) - 3], 2)
for n in range(k2 - 10, k2 + 10):
    s = bin(n)[2:]
    for i in range(3):
        count1 = 0
        count2 = 0
        l = int(s, 2)
        l1 = l
        while l > 0:
            if (l % 10) % 2 == 0:
                count2 += 1
                l //= 10
            elif (l % 10) % 2 != 0:
                count1 += 1
                l //= 10
        if count2 > count1:
            s += '1'
        elif count2 < count1:
            s += '0'
        elif count1 == count2:
            if l1 % 2 == 0:
                s += '0'
            else:
                s += '1'
    r = int(s, 2)
    if 876544 <= r and r <= 1234567899:
        o2 = n
print(o2 - o1 + 1)
