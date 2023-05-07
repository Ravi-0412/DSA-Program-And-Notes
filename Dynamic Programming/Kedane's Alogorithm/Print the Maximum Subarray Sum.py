# time: O(n)= space

def printSubarraySum(arr):
    sumBtIndex= {}    # sum_between_index.  [sum:(start, end)]
    curSum= 0
    start= 0   # will tell from which index we were calculating the curSum in case we will get new ans.
    maxSum= float('-inf')
    for i, n in enumerate(arr):
        if i> 0 and curSum < 0:
            sumBtIndex[curSum]= (start, i-1)
            start= i
            curSum= n
        else:
            curSum+= n
        if i== 0:
            start= i
        sumBtIndex[curSum]= (start, i)
        maxSum= max(maxSum, curSum)
    
    print(sumBtIndex, maxSum)
    i, j= sumBtIndex[maxSum]
    print("maximum SubArray sum: ", arr[i: j+ 1])
            
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr = [-2, -5, 6, -2, -3, 1, 5, -6] 
arr= [-2,-3,-4, -1]
printSubarraySum(arr)


# Time: O(n)
# space: O(1)

def printSubarraySum(arr):
    ansStart, ansEnd= 0, 0   # store the start and endIndex of final ans subArray.
    curSum= 0
    start= 0
    maxSum= float('-inf')
    for i, n in enumerate(arr):
        if i> 0 and curSum < 0:
            start= i
            curSum= n
        else:
            curSum+= n
        if i== 0:
            start= i
        # update our ans index , and maxSum
        if curSum > maxSum:
            ansStart= start
            ansEnd= i
            maxSum= curSum
    
    print(maxSum, ansStart, ansEnd)
    print("maximum SubArray sum: ", arr[ansStart: ansEnd+ 1])
            
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# arr = [-2, -5, 6, -2, -3, 1, 5, -6] 
# arr= [-2,-3,-4, -1]
printSubarraySum(arr)