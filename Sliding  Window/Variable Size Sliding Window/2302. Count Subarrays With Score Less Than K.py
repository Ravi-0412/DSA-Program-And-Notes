# Just exactly same logic as "713. Subarray Product Less Than K".
# After adding each ele, just find the length of valid subarray then that add to 'count'.

# How to take care of CurScore?
# Ans: After adding any ele, find the curScore= (curSum)*(length of subarray)
# when you will move 'i' then update the curSCore also after updating curSum and 'i'.

# time: O(n)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n= len(nums)
        i, j= 0, 0
        curSum= 0
        count= 0
        while j < n:
            curSum+= nums[j]
            curScore= curSum * (j- i + 1)  # current score
            # i should go till 'j' because if there is any ele >='k' itself then we will have to remove all.
            while i<= j and curScore >= k:  
                curSum-= nums[i]
                i+= 1
                curScore= curSum * (j- i + 1)   # update the CurScore
            count+= j - i + 1
            j+= 1
        return count



