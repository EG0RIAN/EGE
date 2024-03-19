for n in range(300):
    s = "1"+"2"*n
    while ("12" in s) or ("5522" in s) or ("2222" in s):
        s = s.replace("12", "55", 1)
        s = s.replace("2222", "1", 1)
        s = s.replace("5522", "21", 1)
    sum = 0
    for i in s:
        sum += int(i)
        if sum == 142:
            print(n)
