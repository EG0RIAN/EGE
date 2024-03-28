digit = (4 ** 2014) + (2 ** 2015) - 8

print(str(bin(digit)[2::]).count("1"))
