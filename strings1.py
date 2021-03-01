''' String Methods '''

a = "Gulzar"
print(a[3])
print(len(a))

for x in a:
    print(x)

''' Check String '''
txt = "This is my sample test"
print('is' in txt)
''' OR '''
if "is" in txt:
    print('Found')
else:
    print('Not Found')

if "is  " not in txt:
    print('Not Found')
else:
    print('Found')

''' Slicing '''
a = 'Gulzar Ahmad Shaik'
print(a[2:7])

''' Start from 0 to 5 '''
print(a[:5])         

''' Start from 2 to end of the string ''' 
print(a[2:])

''' Negative means revers order '''
print(a[-5:-2])

''' strip() will remove any whitespace from the beginning or the end, just like trim '''
b = " Hello World! "
print(b.strip())

print(b.replace("H", "J"))

''' The split() method splits the string into substrings if it finds instances of the separator '''
a = "Hello, World"
print(a.split(','))

'''String Concatenation '''
a = "Hello"
b = "Gulzar"

print(a + b)
c = a + ' ' + b
print(c)

''' format() this method insert number into the string '''
age = 26
txt = "My Name is Gulzar, and I am {}"
print(txt.format(age))

qty = 5
amount = 10
itemno = 112
txt = "I want {} pieces of item {} for {} rupees"
print(txt.format(qty, itemno, amount))

txt = "I want {0} pieces of item {2} for {1} rupees"
print(txt.format(qty, amount, itemno))
