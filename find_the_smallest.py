#You have a positive number n consisting of digits. You can do
# at most one operation: Choosing the index of a digit in the number,
# remove this digit at that index and insert it back to another or at
# the same place in the number in order to find the smallest number you can get.


#best answer by :Aerros

def smallest(n):
    digits = str(n)
    minimum = [n]
    for c1, i in enumerate(digits):
        a = [i for c2, i in enumerate(digits) if c1 != c2]
        for x in range(len(a)+1):
            a.insert(x, i)
            if minimum[0] > int("".join(a)):
                minimum = [int("".join(a)), c1, x]
            del a[x]
    
    return minimum



#smallest(261235) #, [126235, 2, 0]);
#smallest(209917) #, [29917, 0, 1]);
#smallest(285365) #, [238565, 3, 1]);
#smallest(269045) #, [26945, 3, 0]);
smallest(296837) #, [239687, 4, 1]);
#smallest(979972492440540709) #, [97997249244054079, 16, 0]