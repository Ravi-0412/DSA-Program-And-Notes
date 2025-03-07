# logic: 
"""
 count zeros & ones in a binary array and last return minimum between count of zeros & ones by multiplying it with 2. 
 Reason: Since binary array and we are asked to find subsequence(not subarray), so we can take take min(no_one, no_zero) 
 and make a valid subsequence from those numbers. so ans = min(no_one, no_zero) * 2.

 Note: Same Question for longest subarray. (525. Contiguous Array)
"""

# Time = O(n), space = O(1)

def largestSubsequence(arr,n):
    # store count of zeros and one
    countzero = 0
    countone = 0
     
    # traverse binary array and count
    # zeros and ones
    for i in range(n):
        if arr[i]:
            countone += 1
        else:
            countzero += 1
    return min(countone, countzero) * 2


arr = [ 1, 0, 0, 1, 0, 0, 0, 1 ]
n = len(arr)
print("largest Subsequences having" +
        " equal number of 0 & 1 is ",
        largestSubsequence(arr, n))
