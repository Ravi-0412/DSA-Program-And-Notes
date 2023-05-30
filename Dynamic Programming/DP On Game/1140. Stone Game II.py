# just same method we used to find the score of player1 in "486. predict winner". (method 2)

# why here only we need one index para?
# Ans: here we can pick only from start that's why.
# when the index goes out of bound tehn we can simply return '0'.

# Note: 
# piles[i: i+k]=  in case 'i+k' go out of bound then it will give the array from index 'i' to last index.
# And if 'i' goes out of bound then it will give empty array 

# So out of bound cases will get handled automatically, no need to handle separately.

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def FindScore(i, m, turn):
            if i >= len(piles):
                return 0
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, 2*m +1):
                    tempAns= sum(piles[i: i+k]) + FindScore(i +k, max(m, k), False)   # max(m, k) because: we must take max of already picked one . e.g: if m= 3 and k= 1 then can't be less than '3' for any further pick.
                    ans= max(ans, tempAns)   # take max of all possibile chance
                return ans
            else:
                ans= float('inf')
                for k in range(1, 2*m +1):
                    tempAns= FindScore(i +k, max(m, k), True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                return ans

        return FindScore(0, 1, True)


# memoisation
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def FindScore(i, m, turn):
            if i >= len(piles):
                return 0
            if (i, m, turn) in cache:
                return cache[(i, m, turn)]
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, 2*m +1):
                    tempAns= sum(piles[i: i+k]) + FindScore(i +k, max(m, k), False)
                    ans= max(ans, tempAns)   # take max of all possibile chance
                cache[(i, m, turn)]= ans
                return cache[(i, m, turn)]
            else:
                ans= float('inf')
                for k in range(1, 2*m +1):
                    tempAns= FindScore(i +k, max(m, k), True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                cache[(i, m, turn)]= ans
                return cache[(i, m, turn)]
                
        cache= {}
        return FindScore(0, 1, True)
    
# memoisation using 3d array.

# range of 'i': 0 to n  , size: n+1
# range of 'm': if m= n then it can go till 2*n. But weit will get retured automatically when i will go beyond 'n' .so will also work for size 'n+1'
# range of turn: 2(True/false)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def FindScore(i, m, turn):
            if i >= n:
                return 0
            if dp[i][m][turn]!= -1:
                return dp[i][m][turn]
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, 2*m +1):
                    tempAns= sum(piles[i: i+k]) + FindScore(i +k, max(m, k), False)
                    ans= max(ans, tempAns)   # take max of all possibile chance
                dp[i][m][turn]= ans
                return dp[i][m][turn]
            else:
                ans= float('inf')
                for k in range(1, 2*m +1):
                    tempAns= FindScore(i +k, max(m, k), True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                dp[i][m][turn]= ans
                return dp[i][m][turn]
                
        n= len(piles)
        dp= [[[-1 for t in range(2)] for j in range(2*n + 1)] for i in range(n+1)]
        return FindScore(0, 1, True)
