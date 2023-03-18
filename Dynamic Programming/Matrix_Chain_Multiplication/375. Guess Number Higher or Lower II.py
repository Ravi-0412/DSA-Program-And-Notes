# inution behind Q:
# 1) if we have been given the guess function then we could have applied binary search for each number.
# time: O(n*logn)

# logic:  the max means whenever you pick a number, the feedback is always bad and therefore leads you to a worse branch.
#  Since the problem also asks us to "find out how much money you need to have to guarantee a win" we need to assume the worst case scenario.
# vvi: ans will depend on the number you are picking currently and we will pick in such a way that we can guess any of the number in min cost.

# 

# we will only get our ans when we will have only one ele in left subproblem and rigth subproblem. 
# so we will choose in such a way that we can reduce the  our size of subproblem == 1 as soon as possible.
# for minimisng the final ans, we will make incorrect guess for minimum no from the options keeping in mind picking this number will reduce our subproblems to size= 1.

# why MCM type Q?
# Ans: ans will be depend on sequenec of number we pick and we can pick number in any sequence and at last take min of all possible sequences.
# and we can pick any number from '1' to 'n' since we have to find minimum for all cases when we will pick any of the num.

# And if we pick any number then there will be two possiblity(i.e two subproblem) : 1) actual chosen number can be smaller than curr picked.
# 2) actual chosen number can be greater than curr picked number.
# and we have to take max of both the possibilty and finally for ans take min of all the number when we pick.

# we will get our subproblem like this.

# vvi: the maximum number of guessing time should be k = floor(n/2) which means we can find out the right number just using the k nums.
# For example,
# When n = 5, k = floor(5/2) = 2
# we can find out the right number by guessing 2 and 4 as 2 can classify [1, 2, 3] and 4 and classify [3, 4, 5]

# vvi: why total no of guess is not logn?
# Ans: because we can our optimal ans by choosing any of the number not always the middle one.

# https://leetcode.com/problems/guess-number-higher-or-lower-ii/solutions/84778/recursion-memization/
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/solutions/1510747/python-dp-beat-97-52-in-time-99-in-memory-with-explanation/

# time: exponential
class Solution:
    def getMoneyAmount(self, n: int) -> int:

        def minAmount(i, j):  # means minimum money we need to guess all number from 'i' to 'j'.
            if i>= j:   # means there is only one num or no number. suppose there is more than '1' ele and if we choose '1' then i= 1 and j= 0. so include >= instead of "==".
                return 0
            ans= float('inf')
            for k in range(i, j+1):
                tempAns=  k + max(minAmount(i, k-1) , minAmount(k+1, j))  # 'k' is the penalty for choosing incorrectly and we have to get the worst case so consider maximum one i.e max of lower or greater
                ans= min(ans, tempAns)   # take minimum of all possibility.
            return ans

        i,j = 1, n   # both including
        return minAmount(i, j)

# memoising.
# time: O(n^3), space: O(n^2)

# i: from 1 to n+1 (>=j). size= (n+2), j= n to 0 (i>=j). size= (n+1).. (n+2)*(n+1)

class Solution:
    def getMoneyAmount(self, n: int) -> int:

        def minAmount(i, j, dp):
            if i>= j:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]
            ans= float('inf')
            for k in range(i, j+1):
                tempAns=  k + max(minAmount(i, k-1, dp) , minAmount(k+1, j, dp))
                ans= min(ans, tempAns)
            dp[i][j]= ans
            return dp[i][j]

        dp= [[-1 for j in range(n+1)] for i in range(n+2)]
        i,j = 1, n
        return minAmount(i, j, dp)

# tabulation we can do like as usual.


# note: later try to also find the picked number that will lead to minimum cost.