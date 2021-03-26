n = int(input('Enter the Number:'))

listn = [int(i) for i in str(n)]

large = int(max(listn))
strong = []
i = 1
strng = 1
while i <= large:
    strng = i * strng
    strong.append(strng)
    i += 1

new1 = 0
for j in listn:
    new1 = new1 + strong[j-1]

if n == new1:
    print('Given number is Strong number')
else:
    print('Given number is not Strong number')