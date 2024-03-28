def foo(n):
    if n > 2024:
        return n
    if n <= 2024:
        return (n*foo(n + 1))


print(foo(2022)//foo(2024))
