from itertools import product
setik = ""
counter = 1
word_count = 0
for x in product("ФЛАМИНГО", repeat=8):
    setik = "".join(x)
    if (counter % 2 != 0) and (setik[0] != "Н") and (setik.count("О") <= 1):
        word_count += 1
    counter += 1

print(word_count)

# 5714380
