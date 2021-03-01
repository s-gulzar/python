
def oned(num) :

    if num == '1':
        return "One"
    if num == '2':
        return "Two"
    if num == '3':
        return "Three"
    if num == '4':
        return "Four"
    if num == '5':
        return "Five"
    if num == '6':
        return "Six"
    if num == '7':
        return "Seven"
    if num == '8':
        return "Eight"
    if num == '9':
        return "Nine"
    else:
        return "Zero"
    return

def twod(num) :
    if num > 10 and num < 20:
        text1 = tens(num)

    if num == 10:
        text1 = "Ten"
    if num == 20:
        text1 = "Twenty"
    if num == 30:
        text1 = "Thirty"
    if num == 40:
        text1 = "Fourty"
    if num == 50:
        text1 = "Fifty"
    if num == 60:
        text1 = "Sixty"
    if num == 70:
        text1 = "Seventy"
    if num == 80:
        text1 = "Eighty"
    if num == 90:
        text1 = "Ninty"
    return text1


def nexthundred(num):
    if num == 3:
        text2 = "Hundred"
    if num == 4:
        text2 = "Thousand"
    if num == 5:
        text2 = "Lakhs"
    return text2

def tens(num):
    if num == 11:
        text3 = "Eleven"
    if num == 12:
        text3 = "Twelve"
    if num == 13:
        text3 = "Thirteen"
    if num == 14:
        text3 = "Fourteen"
    if num == 15:
        text3 = "Fifteen"
    if num == 16:
        text3 = "Sixteen"
    if num == 17:
        text3 = "SevenTeen"
    if num == 18:
        text3 = "Eighteen"
    if num == 19:
        text3 = "Ninteen"
    return text3




num1 = input('Enter the Number: ')
print(num1)


for x in str(num1):
    words = oned(x)
    words += ' ' + nexthundred(len(num1))

    


    print(words)

'''
if len(num1) == 1:
    oned(num1))

if len(num1) == 2:
    twod(int(num1))
'''
