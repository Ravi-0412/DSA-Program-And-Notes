# 1st method
# By brute force : Check each window of size k and calculate the sum of that window.
# Time:  O(n*k)

def maximumSumSubarray(K, Arr, N):
    max_sum = 0

    # Loop over each possible window of size k
    for i in range(N - K + 1):
        current_sum = 0
        for j in range(i, i + K):
            current_sum += Arr[j]
        max_sum = max(max_sum, current_sum)

    return max_sum


# 2nd method: 
# By Sliding Window

# little concise way of writing the above code
# once you reach that window size, just keep updating your ans and remove the ele at 'i'th index from sum and incr 'i'
# Note vvvvi: At any instant curSum= sum of ele till index 'j' - sum of ele before index 'i'.
# it just represents sum of ele from index 'i' to index 'j'.  i.e prefixSum[j] - prefixSum[i-1]

# time: O(n), space: O(1)

def maximumSumSubarray (self,K,Arr,N):
        i,j,sum1,max_sum= 0,0,0,-9999999999
        while j<N:
            sum1+= Arr[j]
            if j+1>=K:     # or j -i + 1 >= k:
                # Now we have reached the size 'k' so we can start updating our ans.
                max_sum= max(sum1, max_sum)
                sum1-= Arr[i]
                i+= 1
            j+= 1
        return max_sum


# Extension: 

# Q: Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

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

