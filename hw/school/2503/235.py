for N in range(1,1000):
    n = bin(N)[2::]
    if n[-1] == '0':
        n = n + bin(n.count('1'))[2::]
    else:
        n = '1' + n + '00'
    r=int(n,2)
    if r>215:
        print(N)

# 23
