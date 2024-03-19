for x in "0123456789ABCDEFGHIJKLM":
    chislo_one = f"2{x}{x}341011"
    chislo_two = f"220{x}4"
    chislo_three = f"110{x}6"
    itogo = int(chislo_one, 23) + int(chislo_two, 23) + int(chislo_three, 23)
    if itogo % 22 == 0:
        print(itogo//22)
        break
