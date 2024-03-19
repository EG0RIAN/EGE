from itertools import product
counter = 1
itog = 0
for i in product("РЕПЛИКА", repeat=6):
    str_tup = ''.join(i)
    if (counter % 2 == 0) and (str_tup[1] != "К") and (str_tup.count("И") >= 2):
        itog += 1
    counter += 1

print(itog)
