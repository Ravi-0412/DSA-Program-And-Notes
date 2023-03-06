# just same as "Q no: 668".
# Differenec in both: Here we need to sort the array to find no of  absolute difference in less than a given 'num' in  O(n) rather than o(n^2) in unsorted array.

# learnt way to find the absolute diff between pairs in array in O(n*logn).

# logic to find the absolute difference between pairs(here count function):
# Both pointers go from leftmost end. If the current pair pointed at has a distance less than or equal to distance,
# all pairs between these pointers are valid (since the array is already sorted), we move forward the fast pointer. 
# Otherwise, we move forward the slow pointer. By the time both pointers reach the rightmost end, we finish our scan and see if total counts exceed k.

# time: O(n*log(A)). A= max(nums)- min(nums)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # to calculate the no of  absolute difference in less than a given 'num' in  O(n) rather than o(n^2) in unsorted array.
        n= len(nums)

        # uses the two pointer approach.
        def count(num):   # will give the count for which absolute difference between between pairs is <= num.
            i, j, cnt= 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j]- nums[i] <= num:
                    j+= 1
                # add all the indices from 'i' to 'j'. '-1' for absolute diff between same index.
                cnt+= j- i - 1
                i+= 1   # incr 'i' as we can get more ans since after incr 'i' absolute diff will become smaller.
            return cnt

        start= 0  # min Absolute difference we can have = 0
        end=   nums[-1]- nums[0]   # max Absolute difference we can have
        while start < end:
            mid= start + (end- start)//2
            if count(mid) >= k:
                end= mid
            else:
                start= mid + 1
        return start
