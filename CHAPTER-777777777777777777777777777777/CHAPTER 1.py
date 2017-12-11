mylist = [0,2,3,7,11,12]
def count_odd(mylist):
    sb = 0
    for i in mylist:
        if i % 2 == 1:
            sb += 1
    print(sb)

def count_even(mylist)