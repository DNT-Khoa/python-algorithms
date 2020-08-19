# Given two numbers, find their product using recursion

x = 200
y = 20000

def recursive_product(a, b):
    if a == 0:
        return 0

    if a > b:
        return a + recursive_product(b-1, a)

    return b + recursive_product(a - 1, b)

print(recursive_product(x, y))