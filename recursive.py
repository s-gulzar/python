def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

a= 5
print("Factorial of ", a ," is:", factorial(a))


def naturalnum(x):
    if x == 1:
        return 1
    else:
        return x + naturalnum(x - 1)

b = 6
print("Sum of ",b, "Natural Numbers:",naturalnum(b))