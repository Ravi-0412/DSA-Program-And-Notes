# 1st method:
#  time= o(n^2) ,space= o(n)

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n= len(nums)
        target=[]
        for i in range(n):
            target.insert(index[i],nums[i])  # O(n) each time
        return target


# Method 2: Best
# Time: O(n*logn)
# Can done by method of Q : "315. Count of Smaller Numbers After Self".
# Time: O(n* logn)

# Link: https://leetcode.com/problems/create-target-array-in-the-given-order/solutions/549583/o-nlogn-based-on-smaller-elements-after-self/
