# Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Подсчитывается количество чётных и нечётных цифр в десятичной записи заданного числа. Если в десятичной записи больше чётных цифр, то в конец двоичной записи дописывается 1, если нечётных — 0. Если чётных и нечётных цифр в
# десятичной записи поровну, то в конец двоичной записи дописывается 0, если данное число чётное, и 1 — если нечётное.
# 3−4. Пункт 2 повторяется для вновь полученных чисел ещё два раза.
# 5. Результатом работы алгоритма становится десятичная запись полученного числа R.
# Пример. Дано число N = 14. Алгоритм работает следующим образом:
# 1. Строим двоичную запись: 1410 = 11102
# .
# 2. В записи числа 14 чётных и нечётных цифр поровну. Число 14 чётное, дописываем к двоичной записи 0, получаем
# 111002 = 2810
# .
# 3. В записи числа 28 чётных цифр больше, дописываем к двоичной записи 1, получаем 1110012 = 5710
# .
# 4. В записи числа 57 нечётных цифр больше, дописываем к двоичной записи 0, получаем 11100102 = 11410
# .
# 5. Результат работы алгоритма R = 114.
def compare_digits(n):
    chet = 0
    nechet = 0
    for digit in str(int(n, 2)):
        if int(digit) % 2 == 0:
            chet += 1
        else:
            nechet += 1
    if chet > nechet:
        return 1
    if chet == nechet:
        return 2
    return 0


def foo(n):
    s = str(bin(n)[2::])
    for _ in range(2):
        if compare_digits(s) == 1:
            s += "1"
        if compare_digits(s) == 0:
            s += "0"
        if compare_digits(s) == 2:
            if int(s, 2) % 2 == 0:
                s += "0"
            if int(s, 2) % 2 != 0:
                s += "1"
    return int(s, 2)


print(foo(14))