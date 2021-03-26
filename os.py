import os


def curdir():
    return os.getcwd()

print("Current Working Directory:", curdir())


print(curdir())

list1 = os.listdir(curdir())
print(list1)

#Change Current Directory
os.chdir('../') 

