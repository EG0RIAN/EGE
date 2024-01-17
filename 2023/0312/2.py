k = 0
for n in range(765432010, 1542613235):
    if n % 3 != 0 and (n-1) % 3 != 0:
        k += 1

print(k)
