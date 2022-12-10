# Recursive way
# we are breaking when we see any operator(before that).
# since expression can give 'True' even when we will get "False" also.
# so para 'i' and 'j' is not sufficient, we need one more para like what we want i.e eithher 'True' or 'False'. 
class Solution:
    def countWays(self, N, S):
        i, j= 0, N-1
        return self.ways(S, i, j, 1)   # 4th para: isTrue i.e what we want
    
    def ways(self, s, i, j, isTrue):
        if i== j:
            if isTrue: # if we want true 
                if s[i]== 'T':
                    return 1
                else:
                    return 0
            else:  # if we want false
                if s[i]== 'F':
                    return 1
                else:
                    return 0
                    
        count= 0
        for ind in range(i+1, j, 2):
            # now divide into four subproblem 'True' and 'False' for each left and right subdivide array
            LT= self.ways(s, i, ind-1, 1)   # left True
            LF= self.ways(s, i, ind-1, 0)   # Left False
            RT= self.ways(s, ind+1, j, 1)   # left True
            RF= self.ways(s, ind+1, j, 0)   # left True
            if s[ind]==  '&':
                if isTrue:  # both right and left should be True
                    count+= LT * RT
                else: # either right is False, or either left is False or either both is False 
                    count+=  LT * RF + RT* LF + LF* RF
            elif s[ind]== '|':
                if isTrue:  # either both is True or either left is True or either right is True.
                    count+= LT * RT + LT * RF + LF * RT
                else: # both right and left should be False
                    count+=  LF * RF 
            else: # operator is '^'
                if isTrue:   # either only left is True or either only right is True.
                    count+= LT * RF + RT * LF 
                else: # both right and left should be either True or False. 
                    count+=  LT * RT + LF* RF
        return count


# memoization
class Solution:
    def countWays(self, N, S):
        i, j= 0, N-1
        dp= [[[-1 for k in range(2)] for j in range(N)] for i in range(N)]
        return self.ways(S, i, j, 1, dp)   # 4th para: isTrue i.e what we want. we want True 
    
    def ways(self, s, i, j, isTrue, dp):
        if i== j:
            if isTrue: # if we want true 
                if s[i]== 'T':
                    return 1
                else:
                    return 0
            else:  # if we want false
                if s[i]== 'F':
                    return 1
                else:
                    return 0
                    
        if dp[i][j][isTrue]!= -1:
            return dp[i][j][isTrue]
        count= 0
        for ind in range(i+1, j, 2):
            # now divide into four subproblem 'True' and 'False' for each left and right subdivide array
            LT= self.ways(s, i, ind-1, 1, dp)   # left True
            LF= self.ways(s, i, ind-1, 0, dp)   # Left False
            RT= self.ways(s, ind+1, j, 1, dp)   # left True
            RF= self.ways(s, ind+1, j, 0, dp)   # left True
            if s[ind]==  '&':
                if isTrue:  # both right and left should be True
                    count= (count+ (LT * RT) %1003) % 1003
                else: # either right is False, or either left is False or either both is False 
                    count=  (count+ (LT * RF)% 1003 + (RT* LF) % 1003 + (LF* RF) % 1003) % 1003
            elif s[ind]== '|':
                if isTrue:  # either both is True or either left is True or either right is True.
                    count= (count + (LT * RT) % 1003 + (LT * RF) % 1003 + (LF * RT) % 1003) % 1003
                else: # both right and left should be False
                    count= (count+ (LF * RF) % 1003) % 1003 
            else: # operator is '^'
                if isTrue:   # either only left is True or either only right is True.
                    count= (count+ (LT * RF) % 1003 + (RT * LF) % 1003) % 1003 
                else: # both right and left should be either True or False. 
                    count= (count+ (LT * RT) % 1003 + (LF* RF) % 1003) % 1003
            dp[i][j][isTrue]= count
        return dp[i][j][isTrue]

    

