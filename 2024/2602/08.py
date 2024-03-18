from itertools import product
setik = ""
counter = 0

for x in product("фаворит", repeat=6):
    setik = "".join(x)
    if (setik[0] == "о") and (setik.count("р") == 2):
        counter += 1

print(counter)
