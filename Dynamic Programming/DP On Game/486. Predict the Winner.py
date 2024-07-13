# time: O(2^n)= 2^20.

# q: if there is atleast one possible way in which player1 can score more then player1 will win.

# logic: we have to maximise the score of player1.
# so if player1 1) choose first ele('i') then next time he can choose  'i+2' or 'j' 
# if player2 choose 'i+1' and 'i+1' or 'j-1' if player2 choose 'j'.
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
        
#         since the 1st plays to maximize his score overall, 1st can get max(nums[i] + min(1.a, 1.b), nums[j] + min(2.a, 2.b))

# time:2^n

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        score1= self.FindScore(nums, 0, n-1)  # finding the max optimal score can player 1 make.
        return score1 >= sum(nums) - score1   # comparing if socre of player1 is >= player2.
    
    def FindScore(self, nums, i, j):
        if i > j:  # no ele to choose
            return 0
        # if i== j:  # only one ele remaining. both indexes are included so.. No need of this
        #     return nums[i]
        return max(nums[i] + min(self.FindScore(nums, i +2, j), self.FindScore(nums, i +1, j-1)),
                nums[j] + min(self.FindScore(nums, i , j-2), self.FindScore(nums, i+1 , j-1)))


# little expalained in more better , above logic.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        score1= self.FindScore(nums, 0, n-1)  # finding the max optimal score can player 1 make.
        return score1 >= sum(nums) - score1   # comparing if socre of player1 is >= player2.
    
    def FindScore(self, nums, i, j):
        if i > j:
            return 0
        # when player1 pick the 1st ele
        start= nums[i] + min(self.FindScore(nums, i +2, j), self.FindScore(nums, i +1, j-1))
        # when player1 pick the 2nd ele
        end=   nums[j] + min(self.FindScore(nums, i , j-2), self.FindScore(nums, i+1 , j-1))
        return max(start, end)


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


# method 2: other way of finding the score of player1.
# logic: when player1 turn we will add the value of choice that he choose
# (since we are finding the score of player1 only) and will take max of choices
# because he will try to maximise his score at his turn.
# And when it is player2 turn then we will not add the score 
# (since it's is score of player2 not player1) and we will take minimum of his choices
# because player1 will get minimum after player2 turn since both are playing optimally.

# just like we will play the game.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        score1= self.FindScore(0, n-1, True, nums)
        return score1>= sum(nums)- score1
    
    def FindScore(self, i, j, turn, nums):
        if i> j:
            return 0
        if i== j:
            return nums[i]
        if turn:   # means player1 turn
            start= nums[i] + self.FindScore(i+1, j, False, nums)
            end=   nums[j] + self.FindScore(i, j-1, False, nums)
            return max(start, end)
        else:  # player 2 turn
            start= self.FindScore(i+1, j, True, nums)   # when player2 chooses 'i'
            end=   self.FindScore(i, j-1, True, nums)   # when player2 chooses 'j'
            return min(start, end)


# method  3:
# in this we are finding the score difference between p1 and p2 in recursive call.
# got submitted without memoisation . But have overlapping subproblem.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        return self.FindScore(nums, 0, n-1, True) >=0  # return True if difference of score between p1 and p2>=0. 
    
    # what will be the difference in score between p1 and p2 when both plays optimally between index 'i' to 'j'.
    def FindScore(self, nums, i, j, turn):  # for player1 turn , it will be true
        if i >j:
            return 0
        if i== j:
            return nums[i]
        if turn:  # means player 1 turn
            start= self.FindScore(nums, i+1, j, False) + nums[i]
            end=   self.FindScore(nums, i, j-1, False)   + nums[j]
            # player1 will try to maximise the score of himself
            return max(start, end)
        else:
            # adding the score of player2 as negative since he will try to minimise the score of player1 optimally..
            start= self.FindScore(nums, i+1, j, True) - nums[i]   
            end=   self.FindScore(nums, i, j-1, True) - nums[j]
            # player2 will try reduce the score of player1 by chossing optimal.
            # so player1 will get minimum of both
            return min(start, end)
    

# memoisation 
    
# Tabulation for above logic
# https://leetcode.com/problems/predict-the-winner/solutions/96828/java-9-lines-dp-solution-easy-to-understand-with-improvement-to-o-n-space-complexity/

# later write tabulation for all problems.