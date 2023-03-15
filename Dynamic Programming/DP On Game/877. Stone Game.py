# totally same as 486. predict winner, so didn't submit.

# both player will play optimally

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n= len(piles)
        AliceScore= self.FindScore(piles, 0, n-1)
        return AliceScore >= sum(piles) - AliceScore
    
    def FindScore(self, nums, i, j):
        if i > j:
            return 0
        if i== j:  # only one ele remaining
            return nums[i]
        return max(nums[i] + min(self.FindScore(nums, i +2, j), self.FindScore(nums, i +1, j-1)),
                nums[j] + min(self.FindScore(nums, i , j-2), self.FindScore(nums, i+1 , j-1)))
