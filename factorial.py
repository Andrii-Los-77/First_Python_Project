def factorial(x):
    if (x == 0 or x == 1):
        return 1
    return x * factorial(x - 1)

x = 5
print(f"Factorial({x}) = {factorial(x)}")
