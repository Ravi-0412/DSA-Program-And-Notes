# note: here in <= we are updating end= mid (we used to do this in >=). But it will work fine only.
# since mid and condition is acting in opposite way like wehn we will incr the mid (condition value associated with mid will decr)  and so on.
# so indirectly (<=) condition is acting as >= condition only.

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
            if isSum(mid) <= threshold:  # max we need to search till here only. search for even more less num since we have to find the first num(smallest num) for which this condition holds.
                end= mid
            else:  # if isSum(mid) > threshold  => then we need to increase our 'mid' since we have to decr the total sum. And incr the mid will lower the sum and vice versa.
                start= mid + 1
        return start
