def getSingle(val) :
    n = int(val)
    unit = ["Zero", "One","Two", "Three","Four","Five", "Six","Seven","Eight","Nine"]
    return unit[n]

def getTwoDigits(val) :
    n = int(val)
    td = ["Ten", "Eleven","Twelve","Thirteen", "Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    return td[n%10]

def getTens(val) :
    n = int(val)
    tm = ["Twenty", "Thirty","Fourty", "Fifty","Sixty", "Seventy","Eighty","Ninty"]
    return tm[n-2]

def getTenPow(pow1) :
    pow = int(pow1)
    power = ["Hundred", "Thousand"]
    return power[pow-2]

def getNumToWord(n):
    if (n >= 0 and n < 10):
        print(getSingle(n), ' ')
    elif (n >= 10 and n < 20):
        print(getTwoDigits(n), ' ')
    elif (n >= 20 and n < 100) :
        print(getTens(n/10), ' ')
        if (n%10 != 0):
            getNumToWord(n%10)
    elif (n >= 100 and n < 1000): 
        print(getSingle(n/100))
        print(getTenPow(2))

        if(n%100 != 0):
            print("And ")
            getNumToWord(n%100)

    elif(n >= 1000 and n <= 32767) :
        getNumToWord(n/1000)
        print(getTenPow(3), ' ')
        if (n%1000 != 0):
            getNumToWord(n%1000)
    else:
        print("Invalid Input")

n = int(input('Enter the number: '))
getNumToWord(n)
