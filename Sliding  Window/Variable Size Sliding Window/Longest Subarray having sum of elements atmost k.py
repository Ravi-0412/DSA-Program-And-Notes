# NOTE: will only work if all number is "+ve".
# logic: just same as "713. Subarray product less than k".
# i.e after adding each ele find the longest valid subarray.


def longestSubarray(arr, k):
    n= len(arr)
    longest= 0
    i, j= 0, 0
    curSum= 0
    while j < n:
        curSum+= arr[j]
        while i < j and curSum > k:
            curSum-= arr[i]
            i+= 1
        longest= max(longest, j - i +1)
        j+= 1
    return longest
        

# arr= [1, 2, 1, 0, 1, 1, 0]
# k= 4

print(longestSubarray(arr, k))

