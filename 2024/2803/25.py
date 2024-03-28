from fnmatch import *

for x in range(3377, 10**8, 3377):
    if fnmatch(str(x), "?79?8*3"):
        print(x, x//3377)

# 17928493 5309
# 27958183 8279
# 67908093 20109
