# logic: 
"""
 count zeros & ones in a binary array and last return minimum between count of zeros & ones by multiplying it with 2. 
"""

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
