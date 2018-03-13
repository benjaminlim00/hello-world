''' a function maxProductThree(num) that returns the maximum product from any three numbers in a
list of integers. The list may contain both positive, zero, negative integers, and duplicates, but the
maximum product can only be either a negative or a positive number. You can assume that the list
contains at least three non-zero numbers so the maximum product will never be zero.
'''


def maxProductThree(num):
    #count number of negatives
    ls = num[:]
    ls = [x for x in ls if x != 0]
    negcount = 0
    
    #finding max product of 3 maximums:
    lstemp = num[:]
    maxls = []
    for x in range(3):
        maxi = max(lstemp)
        maxls.append(maxi)
        lstemp.remove(maxi)
    max3pro = 1
    for num in maxls:
        max3pro *= num
       
    
    
    
    
    
    for numb in ls:
        if numb < 0:
            negcount += 1
    if negcount <= 1: # just find biggest 3 numbers and find product
        
        maxls = []
        for x in range(3):
            maxi = max(ls)
            maxls.append(maxi)
            ls.remove(maxi)
        ans = 1
        for num in maxls:
            ans *= num
        return ans
    else:
        newmax = max([abs(x) for x in ls])
        negls = [x for x in ls if x < 0]
        
        if newmax not in ls: #first negative, so next one negative and last one positive
            negls.remove(-newmax)
            newmax2 = max(negls)
            product = newmax * newmax2
            anss = product * max(ls)
            return anss
        else:
            ls.remove(newmax)
            newmaxagain = max([abs(x) for x in ls])        
            if newmaxagain in ls: # 2nd number is positive so find a third positive number but must compare with 3 max positive ints
                ls.remove(newmaxagain)
                newmaxagain2 = max(ls)
                ansa = newmaxagain * newmaxagain2 * newmax
                if ansa > max3pro:
                    return ansa
                else:
                    return max2pro
                
            if newmaxagain not in ls: #2nd number is negative so find a third negative number but must compare with 3 max positive ints
                negls.remove(-newmaxagain)
                newmaxagain2 = max(negls)
                product = newmax * newmax2
                ansb = product * max(ls)
                if ansb > max3pro:
                    return ansb
                else:
                    return max2pro
                    
    
num=[6,-3,-10,0,2]
print(maxProductThree(num))

num = [-10, -4, 3, 2, 0]
print(maxProductThree(num))
