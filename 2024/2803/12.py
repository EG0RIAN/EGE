
def foo(n):
    x = "4" + str("1"*n)
    while ("31" in x) or ("411" in x) or ("1111" in x):
        if "31" in x:
            x = x.replace("31", "1", 1)
        if "411" in x:
            x = x.replace("411", "13", 1)
        if "1111" in x:
            x = x.replace("1111", "4", 1)
    return x


for x in range(3, 10001):
    result = foo(x)
    count = 0
    for x in range(len(str(result))):
        count += int(x)
    if count == 34:
        print(x)
        break
