# ans: will give final array after splitting but due to copying operation 
# after each element . it will giev tle. 
# so commented that. But it is totally correct.

# Logic: since we to make array in sorted order, and we only make ele smaller 
# so if we go from left to right then, we will not knowing what value will come next.
# so if split from start then we can't make sure that array will be in increasing order.

# Therefore we need to traverse only from right to left.
# Also if split the last ele then again we can't make sure that after splitting the next coming ele array will be in sorted order.

# so we will leave the last ele as it is and will start splitting from 2nd last ele.

# Spliiting logic and explanation in notes. Page: 166



class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        minOperations = 0
        # ans = [nums[-1]]   # will store the actual array after splitting
        prev = nums[-1]
        for i in range(n-2, -1, -1):
            parts = ceil(nums[i] / prev)  # we have to split nums[i]
            curOperations = parts - 1  # to divide into given no of parts we need to perform 'parts -1' operations.
            minOperations += curOperations
            prev = nums[i] // parts    # maximum value we can get at the leftmost split for nums[i].
                                       # Also this will be the minimum value of every parts.
            r = nums[i] % parts        # this much parts out of total 'parts' will have 'prev + 1' value in splitted array on the right
            remaining_parts = parts - r   # value of all these parts from left side of split will be equal to minimum value only i.e prev
            # ans = [prev] * remaining_parts + [prev + 1] * r  + ans
        # print(ans)
        return minOperations


