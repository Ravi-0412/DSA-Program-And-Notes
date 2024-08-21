# Logic:
"""
just same as "31.next permutation".
first add the digit into an array in same order and apply the exact same logic as "31.nextPermuatation".
"""

class Solution:
    def nextGreaterElement(self, num: int) -> int:
        arr = []
        while num:
            r = num % 10
            arr.append(r)
            num //= 10
        nums = arr[::-1].copy()
        return self.nextPermutation(nums)
    
    def nextPermutation(self, nums):
        n = len(nums)
        i= n- 1  # will point to the index such that nums[i] < nums[i-1] from the right.
        # more later you will find 'i' it means more bigger the number is & if i== 0 then num are in decreasing order. 
        j= n- 1  # will point to the index such that nums[j] > nums[i] from the right.

        # 1) first find 'i'.
        while i> 0 and nums[i-1] >= nums[i]:
            i-= 1
        if i== 0:  # no is in descending order.
            return -1
        # 2)  find 'j'.
        while nums[j] <= nums[i-1]:
            j-= 1
        # 3) now swap the 'j' and 'i-1'.
        nums[j], nums[i-1]= nums[i-1], nums[j]
        # 4) reverse the arr from index 'i' to last.
        # return nums[:i] + (nums[i+1:])[::-1]   # this will not work. because 'nums[:i]: create another array but nums[i:] modifies the same arr'.
        nums[i:]= nums[i:][::-1]
        ans = 0
        for i in range(n):
            ans = ans * 10 + nums[i]
        return ans if ans <= (1 << 31) - 1 else -1   