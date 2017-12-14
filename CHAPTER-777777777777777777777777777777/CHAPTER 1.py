mylist = [0,2,3,7,11,12,14,20]
def count_odd(list):
    sb = 0
    for i in list:
        if i % 2 == 1:
            sb += 1
    return sb

def count_even(list):
    sbeven= 0
    for i in list:
        if i % 2 == 0:
            sbeven += i
    return sbeven

def count_negative(list):
    sbnegative = 0
    for i in list:
        if i  < 0:
            sbnegative += i
    return sbnegative