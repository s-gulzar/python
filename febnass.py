n = int(input("Enter the Number: "))

print('0')
i=0
a=1
b=0
c=0
while (i <= n):
    c = a + b

    a = b
    b = c
    i += 1
    print(c)


