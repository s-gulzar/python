import random

'''
Datatypes in Python:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''

''' Get Datatype '''
x = 5
print(type(x))

str1 = "Hello Gulzar"
print(type(str1))

x = 4.5
print(type(x))

x = 1j
print(type(x))

x = ['Gulzar', 'Ahmad', 'Shaik']
print(type(x))

x = ('Gulzar', 'Ahmad', 'Shaik')
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {'name':'Gulzar', 'age' : 25,
     'name':'Shaik', 'age' : 22}
print(x)
print(type(x))

x = {'Gulzar', 'Ahmad','Shaik'}
print(x)
print(type(x))

x = frozenset({'Apple', 'Bannana', 'Grape'})
print(x)
print(type(x))

x = True
print(type(x))

x = b'Hello'
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))


''' Setting specific datatype '''
x = str(123)
print(x)

x = float(20.5)
print(x)

x = complex(2j)
print(x)

x = list(('Gulzar', 'Ahmad', 'Shaik'))
print(x)

x = bool(5)
print(x)

x = frozenset(("apple", "banana", "cherry"))
print(x)

x = set(("apple", "banana", "cherry"))
print(x)

x = dict(name='Gulzar', age = 25)
print(x)

''' Need to import library "random"  '''
print(random.randrange(1, 10))