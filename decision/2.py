'''
Инверсия - not
Конъюнкция - and
Дизъюнкция - or
XOR - !=
Импликация - <=
Эквивалентность - ==
'''

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = int(((x <= y) and (y <= w)) or (z == (x or y)))
                if F == 0:
                    print(x, y, z, w, F)

'''
РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ

x y z w F
0 1 0 0 0
1 0 0 0 0
1 0 0 1 0
1 1 0 0 0
'''