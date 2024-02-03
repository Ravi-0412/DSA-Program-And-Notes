# Brute force: Take xor of all the number. This will give the ans directly.
# Time: O(n)

# method 2: Binary Search
# logic: in correct part before the 'single ele',
#  1st instance of any ele will occur at even index and 2nd instance will ocuur at odd index.
# so first check if this pattern is getting followed till 'mid' or not.and then move accordingly.

# folowing the correct pattern if 1) mid is even then ele at 'mid' and 'mid+1' should be same   OR
# 2) if 'mid' is odd then then ele at 'mid' and 'mid-1' should be same.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, up= 0, len(nums) -1
        while low < up:
            mid= low + (up-low)//2
            # find the matching index of mid ele.
            # if any of these condition is true then till now they are following the right pattern i.e 
             # if first instance is at even index and there is match. so search in next half.
            if (mid % 2==0 and nums[mid]== nums[mid+1]) or mid % 2 ==1 and nums[mid]== nums[mid-1]: 
                low= mid +1
            else:  # mid can also be the ans
                up= mid
        return nums[low]


# understand the solution of bit also.
# https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/1587257/c-easy-intuitive-solution-2-approaches-binary-search-tc-o-log-n-sc-o-1/
