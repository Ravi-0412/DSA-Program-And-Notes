# Totally same as "1140. stone game 2".
# just pass m= 3 and don't change 'm' in cal;ling funtion and also in for loop run till 'm+1' that's it.

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def FindScore(i, m, turn):
            if i >= n:
                return 0
            if turn: # means player1 turn.
                ans= float('-inf')
                for k in range(1, m+ 1):
                    tempAns= sum(stoneValue[i: i+k]) + FindScore(i +k, m, False)
                    ans= max(ans, tempAns)   # take max of all possibile chance
                return ans
            else:
                ans= float('inf')
                for k in range(1, m +1):
                    tempAns= FindScore(i +k, m, True)
                    ans= min(ans, tempAns)   # take minimum of all possible chance
                return ans

        n= len(stoneValue)
        AliceScore= FindScore(0, 3, True)   # initially pass 'm'= 3.
        BobScore=   sum(stoneValue) - AliceScore
        if AliceScore == BobScore:
            return "Tie"
        elif AliceScore > BobScore:
            return "Alice"
        else:
            return "Bob"


# later try by other approaches and write tabulation also for all problems.
