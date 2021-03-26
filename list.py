a = [10,34,55,76,89]
b = ['Gulzar', 'Parveen', 'Sabreen']

for i in range(len(a)):
    print(a[i])

print('Lenght of List', len(a))

print('Max number in List:', max(a))
print('Max string in List:', max(b))

print('Min Number in List:', min(a))
print('Min String in List:', min(b))

print('Sum of the List:', sum(a))
# sum to string is not posible

a.append(10)
print('After append:', a)

c = []

print('Empty list declaration', c)
c.append('Gulzar')
print('After Append String', c)


a.insert(1,99)
print('After Insert with index:', a)

a.append(c)
print('Append will work as add another list as element in list:', a)


a.extend(range(1,20, 5))
print('List Extend Example:', a)


d = [11,22,33,44,55,66,77,88,99,111]
a.extend(d)
print('Mearging another list using extends:', a)

#Pop: this function will remove last element of the list
a.pop()
print('After Pop:', a)

a.pop(1)
print('Pop with indexing value:',a)

a.pop(-1)
print('Pop with neg indexing', a)

#Remove : This function is used to remove the given element values from list
# If the given element not present in a list, then it returns value error

e = [21,31,41,51,61,71,81,91]
e.remove(31)
print('Remove Function:', e)

# Clear : This function is used to remove the all elements

e.clear()
print('Clear Function:', e)

x = a.copy()
print('Copy Function:', a)

print('Count Funtion:', a.count(10))

f = [21,31,41,51,61,71,81,91,2,1,4]

f.sort()
print('Sorinting function, Assending :', f)


f.sort(reverse=True)
print('Sorting Function, Desc:', f)

def myFunc(e):
    return len(e)