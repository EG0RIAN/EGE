from itertools import product

setik = set()

for x in product("012345678", repeat=6):
    string = "".join(x)
    not_chet = string.count("1") + string.count("3") + string.count("5") + string.count("7")
    if (string[0] != "0") and (string.count("4") == 1) and (not_chet == 2):
        setik.add(string)

print(len(setik))
