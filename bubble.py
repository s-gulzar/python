a = [23, 2, 55, 6, 7, 9, 5, 43, 4]
i = 0
n = len(a)
print(a)

while (i < n):
    j = i
    while (j < n - 1):
        print(a)
        if a[i] > a[ j + 1]:
            temp = a[i]
            a[i] = a[j + 1]
            a[j + 1] = temp
        j += 1
    i += 1

print(a)