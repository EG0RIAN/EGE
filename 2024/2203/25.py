from fnmatch import *

for x in range(5171, 10**8, 5171):
    if fnmatch(str(x), "?19*8?3"):
        print(x, x//5171)

11908813 2303
71995833 13923
81975863 15853
91955893 17783