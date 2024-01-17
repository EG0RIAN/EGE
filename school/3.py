from fnmatch import *

for n in range(21, 10**7, 21):
    if fnmatch(str(n), "9?*55*7"):
        print(n, n//21)
