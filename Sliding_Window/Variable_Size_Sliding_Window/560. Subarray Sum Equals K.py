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
# VVI: analyse this Q and previous Q similarity and differences properly
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans,curr_sum= 0,0
        prefix_sum= {0:1}  # will tell that the no of subarray that will give you the req 'diff'
                            # which we can add to get the final ans. for '0' , one way is always possible
        for n in nums:
            curr_sum+= n
            # prefix_sum[curr_sum]= 1+ prefix_sum.get(curr_sum, 0)  
            diff= curr_sum - k  # find the difference
            ans+= prefix_sum.get(diff, 0)  # if diff is present in prefix_sum then it means sum is possible when we remove this extra sum "diff"
                                            # then add with the value of 'diff' as these many times sum= k will be possible and if not present then add 0

            # and add the surr_sum in prefix_sum. if already present then increment the count by its value alo else add with '1'
            prefix_sum[curr_sum]= 1+ prefix_sum.get(curr_sum, 0)  # now add the curr_sum in the prefix_sum
                                                                  # for next iteration
        return ans


# my mistake:
# you have to always store the curr_sum in prefix_sum by incr its count as it will tell the no of ways 
# you can get that curr_sum and that may no of times it should get added into the ans as these curr_sum will may become 'diff' later
# so always check the possible no with the value of  'diff'
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, curr_sum= 0, 0
        prefix_sum= {}
        for i in range(len(nums)):
            curr_sum+= nums[i]
            # prefix_sum[curr_sum]= 1 + prefix_sum.get(curr_sum, 0)  # writing here will give the incorrect ans as it will make the sum possible
                            #  which might not be possible with given values e.g :[1], sum= 0
            if curr_sum== k:    # this will give error because extra sum is '0' and there can be diff ways to form '0'
                ans+= 1
            elif (curr_sum-k) in prefix_sum:
                ans+= prefix_sum[curr_sum-k]
            prefix_sum[curr_sum]= 1 + prefix_sum.get(curr_sum, 0)   # first i was storing simply with index like "longest subarry with sum= k"
        return ans
