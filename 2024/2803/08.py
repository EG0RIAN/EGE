from itertools import product

counter = 0
word_counter = 1

for x in product("ИНТЕГРАЛ", repeat=5):
    if (word_counter % 2 != 0) and (x[0] != "Т") and ((str(x).count("Н") == 1) or (str(x).count("Н") == 2)):
        counter += 1
    word_counter += 1

print(counter)
# 5992