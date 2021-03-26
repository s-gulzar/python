fileptr = False
try:
    fileptr = open("sample.txt")
except:
    fileprt = False

if fileptr:
    print("File is open successfully")
    fileptr.close()
else:
    print("File name is wrong")


#With Statement

with open("list.py","r") as f:
    content = f.read()
    print(content)

with open("New.txt", "w") as f:
    f.write("Sample test text")
    f.close()

#Reading lines using readline() function
fileptr = open("sample.txt","r")
content = fileptr.readline()
content1 = fileptr.readline()

print(content)
#print(content1)
fileptr.close()