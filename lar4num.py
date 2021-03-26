a = int(input('Enter the Number1:'))
b = int(input('Enter the Number2:'))
c = int(input('Enter the Number3:'))
d = int(input('Enter the Number4:'))

if (a > b):
    num1 = a
else:    
    num1 = b

if num1 < c:
    num1 = c

if num1 > d:
    print('Largest Number: ',num1)
else:
    print('Largest Number:', d)

