def foo(n):
    n_str = str(n)
    first = int(n_str[0])**2 + int(n_str[1]) ** 2
    second = int(n_str[1])**2 + int(n_str[2]) ** 2
    if first < second:
        digit = str(second) + str(first)
    else:
        digit = str(first) + str(second)
    return int(digit)


for x in range(100, 1000):
    if foo(x) == 7434:
        print(x)
