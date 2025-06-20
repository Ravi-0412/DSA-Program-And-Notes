# method 1: 

# Q: Given an array of integers, 
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Time: O(n)
# space: O(1)

def printSubarraySum(arr):
    ansStart, ansEnd= 0, 0   # store the start and endIndex of final ans subArray.
    curSum= 0
    start= 0
    maxSum= float('-inf')
    for i, n in enumerate(arr):
        if curSum < 0:
            start= i
            curSum= n
        else:
            curSum+= n
        # update our ans index , and maxSum
        if curSum > maxSum:
            ansStart= start
            ansEnd= i
            maxSum= curSum
    
    print("SubArray with maximum sum ", arr[ansStart: ansEnd+ 1], "with sum: ", maxSum)
            
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# arr = [-2, -5, 6, -2, -3, 1, 5, -6] 
# arr= [-2,-3,-4, -1]
printSubarraySum(arr)