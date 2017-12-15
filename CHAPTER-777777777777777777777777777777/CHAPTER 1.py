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

def countword5(list):
    numword5=0
    for i in list:
        if len(i)==5:
            numword5 += 1
    return numword5

def sum_to_even(list):
    mysum=0
    for i in list:
        if i%2 == 0:
            continue
        mysum += i
    return mysum

def before_sam(lst):
    count=0
    for i in lst:
        if i == "sam":
            count += 1
            break
        count += 1
    return count

def test_suite():
    test(count_odd(mylist)==6)
    test(sum_even(mylist)==10)
    test(sum_negative(mylist)==-95)
    test(countword5(mylist2)==5)
    test(sum_to_even(mylist)==8)
    test(before_sam(mylist2)==3)
/    test(before_sam(listnosam)==4)



test_suite()