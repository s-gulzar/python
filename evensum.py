'''
n = int(input('Enter the n number:'))

sum = 0
for i in range(n+1):
    if i%2 == 0:
        sum = sum + i
    
print('The sum of given n number of even numbers', sum)

'''

'''
n = int(input('Enter the n number :'))

print('Printing list of binary numbers of given n numbers')

for i in range(n+1):
    print(i,')', bin(i))

'''



n = int(input('Enter the n number:'))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()

for i in range(n, 1,-1):
    for j in range(1, i):
        print(j, end=' ')
    print()

