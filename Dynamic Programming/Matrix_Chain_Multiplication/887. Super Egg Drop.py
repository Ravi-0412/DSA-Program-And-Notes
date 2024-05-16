# Just extension of Q : "1884. Egg Drop With 2 Eggs and N Floors".

# just same as "375. Guess Number Higher or Lower II".
# logic: ans will depend on from which floor we start checking for remaining egg and remaining floor.
# We need to try all possibility. 

# will try to drop from each floor. There will be two condition:
#  1) egg brakes on 'i'th floor. 
#  We need to check with 'k-1' eggs and remaining floor to check = 'i-1' i.e f(k-1, i-1).
# because our ans can't lie beyond 'i' so nned to check only 'i-1' floor.

# 2) egg doesn't brake on 'i'th floor.
#  We need to check with 'k' eggs and remaining floor to check = 'n - i'(after 'i') i.e f(k, n -i).

# we can think like given 'k' eggs and 'n' floor, how many minimum no eggs we have to drop to know the required floor.

# Note vvi: Har floor pe worst case lena h maximum of both choices(break or not break) but overall minimise karna h.

# Note :we want the worst possible case between the two sub-problems. 
# And the overall answer is the best (min) of the worst (max) cases.

# Just exactly same as :"1884. Egg Drop With 2 Eggs and N Floors".
# Just added on more varible 'k'.

# Replace k -> 2 to get ans for "1884. Egg Drop With 2 Eggs and N Floors".

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return self.f(k , n)  # it denotes the min no of moves ,given no of eggs 'k' and remaining floor we have to check is 'n'

    def f(self, k, n, dp):
        # 1) if k == 1 go on checking floor from 1 to 'n'(in worst case)
        # 2) if no of floor < = 1 then ans = no of remaining floor.
        if k== 1 or n <= 1:  
            return n
        if dp[k][n]!= -1:
            return dp[k][n]
        # now check from each floor one by one
        ans= float('inf')
        for i in range(1, n + 1): 
            tempAns= 1+ max(self.f(k-1, i-1, dp), self.f(k, n-i, dp))  # to get maximum if we start to drop from this floor.
            ans= min(ans, tempAns)          # for getting overall minimum
        dp[k][n]= ans
        return dp[k][n]
    

# memoization: TLE
# Time Complexity: O((n^2) * k)
# Space Complexity: O(k * n
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp= [[-1 for i in range(n+1)] for j in range(k+1)]
        return self.f(k , n, dp)  # it denotes the given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n, dp):
        # 1) if k == 1 go on checking floor from 1 to 'n'(in worst case)
        # 2) if no of floor < = 1 then ans = no of remaining floor.
        if k== 1 or n <= 1:  
            return n
        if dp[k][n]!= -1:
            return dp[k][n]
        # now check from each floor one by one. No need to check from floor 'n', it will get handled automatically in base case.
        ans= float('inf')
        for i in range(1, n + 1): 
            tempAns= 1+ max(self.f(k-1, i-1, dp), self.f(k, n-i, dp))
            ans= min(ans, tempAns) 
        dp[k][n]= ans
        return dp[k][n]

# optimising memoization using bottom up and binary search.
# Instead of dropping from each possible floor, we can find the floor using binary search.
# Time Complexity: O((n * k) * logn )
# Space Complexity: O(n * k)

# note: understand this approach properly from below links
# https://leetcode.com/problems/super-egg-drop/solutions/792736/cpp-explained-recursive-memoization-optimization-dp-well-explained-easy-to-unserstand/
# https://leetcode.com/problems/super-egg-drop/solutions/159079/python-dp-from-kn-2-to-knlogn-to-kn/
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp= [[-1 for i in range(n+1)] for j in range(k+1)]
        return self.f(k , n, dp)  # it denotes the given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n, dp):
        # 1) if k == 1 go on checking floor from 1 to 'n'(in worst case)
        # 2) if no of floor < = 1 then ans = no of remaining floor.
        if k== 1 or n <= 1:  
            return n
        if dp[k][n]!= -1:
            return dp[k][n]
        # now check from each floor using binary search instead of linear search
        ans= float('inf')
        l, h, tempAns= 1, n, 0
        # just try to bring left and right as close as possible.
        # right and left denote the no of moves for f(k-1, mid) and f(k, n-mid).
        # if right > left then more move in checking 'n-mid' floor so we will update low= mid +1 (since we have to maximise the possible ans).
        # else update l= 'mid+1. we are just moving in part which have more no of moves to maximise the temporary ans.
        while l<= h: 
            mid= (l+h)//2
            left=  self.f(k-1 , mid-1, dp)  # if egg broken, check for down floors of mid..
            right= self.f(k , n- mid, dp)   # if egg doesn't break , check for up floors of mid
            tempAns= 1+ max(left, right)     # store max of both 
            if right > left:  # since right is more than left and we need more in worst case
                l= mid +1    # so l=mid+1 to gain more for worst case : upward
            else: # left >= right so we will go downward 
                h= mid -1
            ans= min(ans, tempAns)  # store minimum attempts
        dp[k][n]= ans
        return dp[k][n]


# method 2:
# Try to understand this also later.
# https://leetcode.com/problems/super-egg-drop/solutions/443089/simplest-python-dp-solution-with-detailed-explanation-99-time-100-mem/
# https://leetcode.com/problems/super-egg-drop/solutions/158974/c-java-python-2d-and-1d-dp-o-klogn/


