# was easy only but thought to the point
# logic: since first and last ele are neighbour so both can't be the part of ans simultaneously
# i.e ans will be conation only one of them 
# so ans will equal to the max(when we exclude the first ele, when we exclude the last ele)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        excluding_last, excluding_first= [], []
        for i in range(len(nums)):
            if i!= 0: 
                excluding_first.append(nums[i])
            if i!= len(nums)-1:
                excluding_last.append(nums[i])
        ans_excluding_last=  self.helper(excluding_last)
        ans_excluding_first= self.helper(excluding_first)
        return max(ans_excluding_last, ans_excluding_first)
                
        
    def helper(self, nums):
        n= len(nums)
        non_adj= 0  # intially it will be zero
        adj= nums[0]  # initially it will be nums[0]
        ans= nums[0]  # in case only one ele is present and also this will be the minimum profit
        for i in range(1,n):
            # when you include curr ele in profit
            take= nums[i]
            if i>=2:  # if you take that ele then add the non_adj
                take+= non_adj
            notTake= adj  # if not take then equate to adj ele
            ans= max(take, notTake)
            adj, non_adj= ans, adj  # curr ele will become 'adj' and adj will become 'non_adj' for next coming ele
        return ans