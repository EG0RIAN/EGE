from fnmatch import *

for x in range(37, 10**9, 37):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x//37)

# 123451758 3336534
# 123454718 3336614
# 123458788 3336724