f = open("17.txt")

a = [int(x) for x in f]

max90 = max([x for x in a if abs(x) % 100 == 90])
res = []
for i in range(len(a) -2):
    if 1000<=abs(a[i])<=9999 or 1000<=abs(a[i+1])<=9999 or 1000<=abs(a[i+2])<=9999:
        s = a[i] + a[i+1] + a[i+2]
        if s > max90:
            res.append(s)
print(len(res),min(res))

# 980 17924