''' 
1) String Formatting 
    a) % Method
    b) Format()
    c) f - String

'''

mycourse = 'Python Course'
print('I am learning %s' %mycourse)

myage = 40
print('My Course is %s my-age %i years' %(mycourse, myage))

print('My Course is %(my-course)s my-age %(my-age)i years' %{'my-course':mycourse, 'my-age':myage})


greetings = 'My Course is {my_course} and my age is {my_age} years'
print(greetings.format(my_course=mycourse, my_age=40))


print('Testing {} with out variable'.format('New'))