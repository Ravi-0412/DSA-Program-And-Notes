# note: here in <= we are updating end= mid (we used to do this in >=). But it will work fine only.
# since mid and condition is acting in opposite way like when we will incr the mid 
# (condition value associated with mid will decr)  and so on.
# So logically we are updating start and end for same reason only like we used to do this in all the Q.

# Vvi Reason: we will get max sum when our mid will less and min sum when our mid will be high.
# vvi Range: start = 1 , when start = 1 then we will get maximum sum
# end= max(sum), we will get minimum sum when our mid= max(nums). we will get sum = len(nums) so threshold >= len(nums)

# time: O(n* log(max(nums)))
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def isSum(mid):  # will give the sum of divisions when all ele in array is divided by 'mid'.
            sum= 0
            for n in nums:
                sum+= math.ceil(n/mid)
            return sum

        start, end= 1, max(nums)
        while start < end:
            mid= start + (end - start)//2
            if isSum(mid) <= threshold:  # if isPossible(mid) =>  then try to get more smaller
                end= mid
            else:  # if isSum(mid) > threshold  => we need to decrease the sum for this we need to increase the mid .
                start= mid + 1
        return start


# my mistake:
# this template most of time lead to TLE by updating start or end by same value again and again.
# Best use above template only. Just use above one acc to the logic of the Q.
# in case we need to decrease our ans (>= or <=) acc to the Q, we will update our end = mid 
# and where we have to increase our ans (< or >), we will update start= mid + 1.
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def isSum(mid):  # will give the sum of divisions when all ele in array is divided by 'mid'.
            sum= 0
            for n in nums:
                sum+= math.ceil(n/mid)
            return sum

        start= 1
        end=  max(nums)
        while start < end:
            mid= start + (end - start)//2
            if isSum(mid) >= threshold:  # max we need to search till here only. search for even more less num since we have to find the first num(smallest num) for which this condition holds.
                start= mid
            else:  # if isSum(mid) > threshold  => then we need to increase our 'mid' since we have to decr the total sum. And incr the mid will lower the sum and vice versa.
                end= mid + 1
        return start