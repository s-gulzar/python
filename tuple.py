tup1 = (12, 34, 56)
tup2 = ('Gulzar', 'Sabreen', 'Parveen')

tup3 = tup1 + tup2

print(tup3)
print(tup3[1])
print(tup3[1:5])
print(tup1[-1])
print(tup3[:2])
print(tup3[2:])
print(tup3[-4:-1])
print('Length:', len(tup3))
print('Type:', type(tup3))


tup4 = ('Apple', 'Bannana', 'Grape')
y = list(tup4)
print(y)
y[1]="Kiwi"

x = tuple(y)
print('Updated Tuple:', x)

#convert tuple to list and update, then convert into tuple
tup5= ("Testing1", "Testing2", "Testing3")
y = list(tup5)
y.append("Orange")
tup5 = tuple(y)
print(y)

#Delete the Tuple
tup6= ("Testing1", "Testing2", "Testing3")
del tup6


#unpacked tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry","Kiwi", "Grapse")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)