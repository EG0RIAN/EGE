a = int(input())
flag = True
b = -1
while a != 0:
    last_digit = a % 10
    if last_digit < b:
        flag = False
    b = last_digit
    a //= 10
if flag == True:
    print("YES")
else:
    print("NO")
