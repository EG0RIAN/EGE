from collections import Counter

n = 3 * (343 ** 8) + 5 * (49 ** 12) + 7 ** 15 - 49
ans = ''
while n != 0:
    ans += str(n % 7)
    n = n // 7
counter = Counter(ans)
print(counter)
