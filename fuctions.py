''' Python function should be write on top and call at bottom as warterfall model'''

''' Function No Aruguments '''
def function1():
    print('This is simple')
''' Calling a Function
    To call a function, use the function name followfunction should be called with open and close braces'''
function1()

''' Function with Arguments '''
def function2(intval):
    print('Argument value : ', intval)
function2(100)

''' Function with multiple Arguments '''
def function3(arg1, arg2, arg3):
    print('Multi Arugments function', arg1, ' ', arg2, ' ', arg3)
    print(type(arg1), ' ', type(arg2), ' ', type(arg3))
function3(123, 'Gulzar', 'Ahmad')

''' Arbitrary Arguments, *args 
    If number of arguments is unknown then add, * before the parameter name'''

def function4(*arg1):
    print('Arbitratry Arguments :', arg1[1])
function4(123, 'Arbitratry')

''' Keyword Arguments '''
def function5(arg3, arg2, arg1):
    print('KeyWord Arguments:', arg1, ' ', arg2, '  ', arg3)

function5(arg1='Testing1', arg3 = 'Testing3', arg2 = 'Testing2')

''' Arbitatry Keyword Arguments 
    If you don't know how many arguments passed to the fuction use ** before function argument name '''

def function6(**args1):
    print('Arbitatory Keyword Arguments: ', args1["lname"])

function6(fname="Gulzar", lname="Shaik")

''' default argument values in function '''
def function7(args1 = 'Gulzar'):
    print('The default argument value example: ', args1)

function7()
function7('Shaik')
function7('Hello')


''' Passing list is an argument'''
def function8(food):
    for x in food:
        print(x)

food = ['Apple', 'Bannana', 'Cherry']
function8(food)

''' Return values in function '''
def function9(x):
    return 5 * x

print(function9(2))

''' The Pass Statement 
    Function definition cannot be empty, but for some reason you need empty function then add pass keyword in to the function'''
def function10():
    pass

function10()


''' Recursion
    A Function called its self '''
def function11(x):
    if (x > 0):
        result = x + function11(x - 1)
        print(result)
    else:
        result = 0
        print(result)
    return result

print('Recursion example')
function11(6)


def function12():
    """  

    This function prints Hello Gulzar 
    
    """
    print("Hello Gulzar")


function12.__doc__

#------------------------------------------------------------------------------------
#Lamada Functions:
#syntax : lambda arguments:expression

x = lambda a: a + 10

print(x)
print("Output:", x(20))

y = lambda a,b: a + b
print("Sum:", y(10,20))