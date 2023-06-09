# NOTE: will only work if all number is "+ve".
# logic: just same as "713. Subarray product less than k".
# i.e after adding each ele find the longest valid subarray.


# def LongestSubarray(arr, k):
#     n= len(arr)
#     i, j= 0, 0
#     curSum= 0
#     ans= 0
#     while j < n:
#         curSum+= arr[j]
#         if curSum <= k:
#             ans= max(ans, j- i + 1)
#         elif curSum > k :
#             while i<= j and curSum > k:
#                 curSum-= arr[i]
#                 i+= 1
#             ans= max(ans, j- i +1)
#         j+= 1
#     return ans

# concise way of above, just same logic as "713. Subarray product less than k".
# After adding any ele find the longest valid subarray.
def LongestSubarray(arr, k):
    n= len(arr)
    i, j= 0, 0
    curSum= 0
    ans= 0
    while j < n:
        curSum+= arr[j]
        # i should go till 'j' because if there is any ele greater than 'k' itself then we will have to remove all.
        while i<= j and curSum > k:  
            curSum-= arr[i]
            i+= 1
        ans= max(ans, j- i +1)
        j+= 1
    return ans


arr= [1, 2, 1, 0, 1, 1, 0] 
k = 4
print(LongestSubarray(arr, k))

# do for negative number also