# time: O(2^n)= 2^20.

# logic: we have to maximise the score of player1.
# so if player1 1) choose first ele('i') then next time he can choose  'i+2' or 'j' if player 2 choose 'i+1' and 'i+1' or 'j-1' if player2 choose 'j'.
# and 2) choose last ele('j') then next time he can choose 'i' or 'j-1' if player 2 choose 'j-1' and 'i+1' or 'j-1' if player2 choose 'i'.

# vvi: since 2nd player will maximise his score in every move then 1st player will get min of two cases after player2 choose.
# and finally player1 will maximise his score so he will take max of all the cases.

# https://leetcode.com/problems/predict-the-winner/solutions/155217/from-brute-force-to-top-down-dp/

# How to approach?
# Ans: just find the max number of score player1 can make when both player plays optimally.
# At last compare this score with score of player2. score of player2= sum(nums)- player1_score.

# logic to find the max score of player1:

# currently 1st with choosable i, j,
#         1.if 1st picks nums[i], 2nd can pick either ends of nums[i + 1, j]
#             a.if 2nd picks nums[i + 1], 1st can pick either ends of nums[i + 2, j]
#             b.if 2nd picks nums[j], 1st can pick either ends of nums[i + 1, j - 1]
#             since 2nd plays to maximize his score, 1st can get nums[i] + min(1.a, 1.b)
						
#         2.if 1st picks nums[j], 2nd can pick either ends of nums[i, j - 1]
#             a.if 2nd picks nums[i], 1st can pick either ends of nums[i + 1, j - 1];
#             b.if 2nd picks nums[j - 1], 1st can pick either ends of nums[i, j - 2];
#             since 2nd plays to maximize his score, 1st can get nums[j] + min(2.a, 2.b)
        
#         since the 1st plays to maximize his score, 1st can get max(nums[i] + min(1.a, 1.b), nums[j] + min(2.a, 2.b))


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
# time: O(n^2)= space
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
