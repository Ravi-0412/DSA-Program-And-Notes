# time: O(2^n)= 2^20.

# logic: we have to maximise the score of player1.
# so if player1 1) choose first ele('i') then next time he can choose  'i+2' or 'j' if player 2 choose 'i+1' and 'i+1' or 'j-1' if player2 choose 'j'.
# and 2) choose last ele('j') then next time he can choose 'i' or 'j-1' if player 2 choose 'j-1' and 'i+1' or 'j-1' if player2 choose 'i'.

# vvi: since 2nd player will maximise his score in every move then 1st player will get min of two cases after player2 choose.
# and finally player1 will maximise his score so he will take max of all the cases.

# https://leetcode.com/problems/predict-the-winner/solutions/155217/from-brute-force-to-top-down-dp/

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        score1= self.FindScore(nums, 0, n-1)  # finding the max optimal score can player 1 make.
        return score1 >= sum(nums) - score1   # comparing if socre of player1 is >= player2.
    
    def FindScore(self, nums, i, j):
        if i > j:
            return 0
        if i== j:  # only one ele remaining
            return nums[i]
        return max(nums[i] + min(self.FindScore(nums, i +2, j), self.FindScore(nums, i +1, j-1)),
                nums[j] + min(self.FindScore(nums, i , j-2), self.FindScore(nums, i+1 , j-1)))


# memoisation:
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        dp= [[-1 for j in range(n)] for i in range(n)]
        score1= self.FindScore(nums, 0, n-1, dp)
        return score1 >= sum(nums) - score1
    
    def FindScore(self, nums, i, j, dp):
        if i== j:  # only one ele remaining
            return nums[i]
        if i > j:
            return 0
        if dp[i][j]!= -1:
            return dp[i][j]
        dp[i][j]= max(nums[i] + min(self.FindScore(nums, i +2, j, dp), self.FindScore(nums, i +1, j-1, dp)),
                nums[j] + min(self.FindScore(nums, i , j-2, dp), self.FindScore(nums, i+1 , j-1, dp)))
        return dp[i][j]
