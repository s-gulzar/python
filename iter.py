#iter and next demonstration
#basic use of iter()

lst = [11,22,33]
iter_lst = iter(lst)

try:
    print(next(iter_lst))
    print(next(iter_lst))
    print(next(iter_lst))
    print(next(iter_lst))
except:
    pass
