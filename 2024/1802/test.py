def solve(n, products, t, actions):
    store = {product[0]: int(product[1]) for product in products}
    cart = {}
    for action in actions:
        operation, product_name = action
        if operation == '+':
            if store.get(product_name, 0) > 0:
                cart[product_name] = cart.get(product_name, 0) + 1
                store[product_name] -= 1
        elif operation == '-':
            if cart.get(product_name, 0) > 0:
                cart[product_name] -= 1
                store[product_name] += 1
                if cart[product_name] == 0:
                    del cart[product_name]
    for product_name in sorted(cart.keys()):
        print(f'{product_name} {cart[product_name]}')


n = int(input())
products = [input().split() for _ in range(n)]
t = int(input())
actions = [input().split() for _ in range(t)]

solve(n, products, t, actions)

###

import re

def validate(name, surname, phone):
    if not re.match(r'^[A-Z][a-z]{0,24}$', name) or not re.match(r'^[A-Z][a-z]{0,24}$', surname):
        return 'no'
    if not re.match(r'^\+7\d{10}$', phone):
        return 'no'
    return 'yes'

test_count = int(input())
for i in range(test_count):
    name = input()
    surname = input()
    phone = input()
    print(validate(name, surname, phone))
