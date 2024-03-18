from itertools import product

count = set()

for s in product("игорь", repeat=8):
    if (s[0] != "ь") and (s.count("о") == 1) and (s.count("ь") == 1):
        slovo = "".join(s)
        count.add(slovo)

print(len(count))
