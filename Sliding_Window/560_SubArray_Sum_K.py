# brute force
# time: O(n^2)
def SubArray_Sum(arr,k):
    ans= 0
    for i in range(len(arr)):
        wind_sum= 0
        for j in range(i,len(arr)):
            wind_sum+= arr[j]
            if wind_sum== k:
                ans+= 1  
    return ans

# arr= [10, 2, -2, -20, 10]
# k = -10 
arr = [9, 4, 20, 3, 10, 5]
k = 33
# arr= [1,2,3]
# k= 3
# arr= [1,1,1]
# k= 2
# print(SubArray_Sum(arr,k))     


# sliding window but is not valid for negative numbers
# don't getting the correct output, tried a lot(got was missing one condition)
# time : O(n)
def Count_SubArray(arr,k):
    i,j,win_sum,ans= 0,0,0,0
    while j<len(arr):
        win_sum+= arr[j]
        if win_sum== k:
            ans+= 1
        elif win_sum >k:
            # first make sum <k(and keep on incr 'i') then incr 'j'
            # just shifting the window for finding the ans like before
            while win_sum >k:  # in thgis you have to delete from left since all are positive no
                win_sum-= arr[i]
                i+= 1
                # while removing win_sum can become equla to 'k' also
                if win_sum== k:
                    ans+= 1
        j+= 1  # you have to incr 'j' always so better write outside the loop
    return ans

# arr = [9, 4, 20, 3, 10, 5]
# k = 33
# arr= [1,2,3]
# k= 3
arr= [1,1,1,1,2,1]
k= 3
print(Count_SubArray(arr,k))


# better one:
# time: O(n)
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ans,curr_sum= 0,0
#         prefix_sum= {0:1}  # will tell that the no of subarray that will give you the req 'diff'
#                             # which we can add to get the final ans
#         for n in nums:
#             curr_sum+= n
#             diff= curr_sum - k  # find the difference
#             ans+= prefix_sum.get(diff, 0)  # add the count of that diff in the ans(no of subarray possible with that diff)
#             prefix_sum[curr_sum]= 1+ prefix_sum.get(curr_sum, 0)  # now add the curr_sum in the prefix_sum
#                                                                   # for next iteration
#         return ans

