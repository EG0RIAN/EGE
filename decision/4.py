#ИЗ ДЕСЯТИЧНОЙ СИСТЕМЫ СЧИСЛЕНИЯ

#В ДВОИЧНУЮ

print(bin(123))
#0b1111011
print(bin(123)[2:])
#1111011

#В ВОСЬМЕРИЧНУЮ

print(oct(123))
#0o173
print(oct(123)[2:])
#173

#В ШЕСТНАДЦАТЕРИЧНУЮ

print(hex(123))
#0x7b
print(hex(123)[2:])
#7b

#В ЛЮБУЮ

def perevod(num, osn):
    values = '0123456789ABCDEF'
    result = ''
    while num > 0:
        result = values[num % osn] + result
        num = num // osn
    return result

print(perevod(123, 9))
#146

#В ДЕСЯТИЧНУЮ

print(int('1111011', 2))
#123
print(int('173', 8))
#123
print(int('7b', 16))
#123
print('146', 9)
#123