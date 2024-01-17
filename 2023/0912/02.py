def foo(n, k):
    if n == k:
        return 1
    if n > k or n == 17:
        return 0

    return foo(n+2, k)+foo(n+3, k)+foo(n*2, k)


print(foo(3, 10)*foo(10, 25))
