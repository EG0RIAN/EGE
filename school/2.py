from fnmatch import *

for n in range(161, 10**8, 161):
    if fnmatch(str(n), "12*4?65"):
        print(n, n//161)
