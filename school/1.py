from fnmatch import *

for n in range(51, 10**6, 51):
    if fnmatch(str(n), "12*4?65"):
        print(n, n//51)


# 122145 2395
# 122451 2401
# 124542 2442
# 124593 2443
# 127245 2495