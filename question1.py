a = ["What is the values of 2X2?", "What is the value of 3X3?", "What is the value of 4X4?"]
b = [4, 9, 16]
c = [[2, 3, 4, 6], [7, 12, 9, 8], [15, 12, 16, 21]]
d = ['a', 'b', 'c', 'd']

ans = 0

for i in range(len(a)):
    print(a[i])
    for j in range(len(c[i])):
        print(d[j], ")", c[i][j])
    n = input("Please enter the option:")
    if d.count(n) > 0:
        ind1 = d.index(n)
        ind2 = c[i].index(c[i][ind1])
        if c[i][ind2] == b[i]:
            print("Answer is correct")
            ans += 1
        else:
            print("Answer is wrong")
        print()
    else:
        print("Invalid option") 


print("Total correct answers:", ans)