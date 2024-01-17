x = 3*(216**4) + 2*(36**6) - 648
s = ''
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]
print(s.count("5"))
