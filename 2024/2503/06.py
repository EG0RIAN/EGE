setik = set()
for x in "0123456789ABCDEFGHIJKLMNO":
    result = int(f"1{x}2{x}3{x}4{x}5", 25) + int(f"2{x}024", 25) + int(f"1{x}099", 25)
    if result % 24 == 0:
        setik.add(result // 24)

print(max(setik))

# 159191846568
