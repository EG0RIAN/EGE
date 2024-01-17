for N in range(100):
    s = bin(N)[2:]
    sum = s.count('1')
    s = s + str(sum % 2)
    sum = s.count('1')
    s = s + str(sum % 2)
    R = int(s, 2)
    if R > 77:
        print(N)
        break
