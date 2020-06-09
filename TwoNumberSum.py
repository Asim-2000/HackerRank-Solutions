#time=O(n^2)|space=O(1)
def twoNumberSum(array,targetsum):
    for i in range(len(array)-1):
        firstnum=array[i]
        for j in range(i+1,len(array)):
            secondnum=array[j]
            if (firstnum+secondnum==targetsum):
                return[firstnum,secondnum]

    return[]

#time=O(n)|space=O(n)
def twoNumberSum2(array,targetsum):
    map={}
    for number in map:
        potentialmatch=targetsum-number
        if (potentialmatch in map):
            return [potentialmatch,number]
            #otherwise, we will add the number in the dictionary with value true
        else:
            map[number]=True
    return []

#time=O(nlog(n)) | space=O(1)
def twoNumberSum3(array,targetsum):
    array.sort()
    left=0
    right=len(array)-1
    while left < right:
        currentsum=array[left]+array[right]
        if currentsum==targetsum:
            return [array[left],array[right]]
        elif currentsum < targetsum:
            left+=1
        elif currentsum > targetsum:
            right-=1
    return []
