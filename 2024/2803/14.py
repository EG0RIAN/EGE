
setik = set()
for x in range(1000):
    result = int(f"3{x}2{x}1{x}0{x}1", 19) + int(f"{x}2024", 19) + int(f"1{x}077", 19)
    if x == 997:
        print(result//18)
# 56080297085254625570
