# i am getting how to do but.

# just start dropping egg from floor 1 for better utilisation of given egg and if breaks then required floor is '0' (1-0) 
# and if doesn't break go on checking for next floor. But this will only work if we were given one egg only. 

# doubt: i am not geing how to check whether any egg break or not after dropping.

# simple way: start checking with 'k' eggs and 'n' floor.
# start checking from 1st floor , if breaks then we only need to check till one floor before with 'k-1' eggs
# and if doesn't break then go on checking for higher floor with same egg. 
# links:
# https://leetcode.com/problems/super-egg-drop/solutions/792736/cpp-explained-recursive-memoization-optimization-dp-well-explained-easy-to-unserstand/
# https://leetcode.com/problems/super-egg-drop/solutions/159079/python-dp-from-kn-2-to-knlogn-to-kn/
# https://leetcode.com/problems/super-egg-drop/solutions/443089/simplest-python-dp-solution-with-detailed-explanation-99-time-100-mem/
# https://leetcode.com/problems/super-egg-drop/solutions/158974/c-java-python-2d-and-1d-dp-o-klogn/

# videos: 
# https://www.youtube.com/watch?v=iOaRjDT0vjc
# Note: we have eggs always greater than '0'.

# we can think like given 'k' eggs and 'n' floor, how many minimum no eggs we have to drop to know the required floor.
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return self.f(k , n)  # it denotes the min no of moves ,given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n):
        if n== 0 or n== 1:  # if remaining floor is '0' or '1' then we need '0' or '1' move respectively.
            return n
        if k== 1:  # go on checking floor from 1 to 'n'(in worst case)
            return n
        # now check from each floor one by one
        ans= inf
        for i in range(1, n): # start checking from 1st floor otherwise you will left with no egg to check further
            # if egg break then we need to check till 'n-1' with 'k-1' egg and
            #  if doesn't then remaining floor to check will be 'n-i' with 'k' eggs as we have to find max floor
            tempAns= 1+ max(self.f(k-1, i-1), self.f(k, n-i))
            ans= min(ans, tempAns)  # for getting the minimum floor no
        return ans

# memoization: TLE
# Time Complexity: O((n^2) * k)
# Space Complexity: O(k * n
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp= [[-1 for i in range(n+1)] for j in range(k+1)]
        return self.f(k , n, dp)  # it denotes the given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n, dp):
        if n== 0 or n== 1:  # if remaining floor is '0' or '1' then we need '0' or '1' move respectively.
            return n
        if k== 1:  # go on checking floor from 1 to 'n'(in worst case)
            return n
        if dp[k][n]!= -1:
            return dp[k][n]
        # now check from each floor one by one
        ans= inf
        for i in range(1, n):
            # if egg break then we need to check till 'n-1' with 'k-1' egg and
            #  if doesn't then remaining floor to check will be 'n-i' with 'k' eggs as we have to find max floor
            tempAns= 1+ max(self.f(k-1, i-1, dp), self.f(k, n-i, dp))
            ans= min(ans, tempAns)  # for getting the minimum floor no
        dp[k][n]= ans
        return dp[k][n]

# checking the sub function also whether already calculated or not to reduce the recursion depth.
# still giving TLE
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp= [[-1 for i in range(n+1)] for j in range(k+1)]
        return self.f(k , n, dp)  # it denotes the given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n, dp):
        if n== 0 or n== 1:  # if remaining floor is '0' or '1' then we need '0' or '1' move respectively.
            return n
        if k== 1:  # go on checking floor from 1 to 'n'(in worst case)
            return n
        if dp[k][n]!= -1:
            return dp[k][n]
        # now check from each floor one by one
        ans= inf
        for i in range(1, n):
            # if egg break then we need to check till 'n-1' with 'k-1' egg and
            #  if doesn't then remaining floor to check will be 'n-i' with 'k' eggs as we have to find max floor
            # optimising the lower level function call
            if dp[k-1][i-1]!= -1:
                low= dp[k-1][i-1]
            else:
                low= self.f(k-1, i-1, dp)
                dp[k-1][i-1]= low
            # optimising the higher level function call
            if dp[k][n-i]!= -1:
                high= dp[k][n-i]
            else:
                high= self.f(k, n-i, dp)
                dp[k][n-i]= high

            tempAns= 1+ max(low, high)
            ans= min(ans, tempAns)  # for getting the minimum floor no
        dp[k][n]= ans
        return dp[k][n]

# optimising memoization using bottom up and binary search
# here we find the move for mid floor and then take the decision accordingly.
# Time Complexity: O((n * k) * logn )
# Space Complexity: O(n * k)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp= [[-1 for i in range(n+1)] for j in range(k+1)]
        return self.f(k , n, dp)  # it denotes the given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n, dp):
        if n== 0 or n== 1:  # if remaining floor is '0' or '1' then we need '0' or '1' move respectively.
            return n
        if k== 1:  # go on checking floor from 1 to 'n'(in worst case)
            return n
        if dp[k][n]!= -1:
            return dp[k][n]
        # now check from each floor using binary search instead of linear search
        ans= inf
        l, h, tempAns= 1, n, 0
        while l<= h: 
            mid= (l+h)//2
            left=  self.f(k-1 , mid-1, dp)  # if egg breaks
            right= self.f(k , n- mid, dp)   # if egg doesn't break
            tempAns= 1+ max(left, right)
            if right> left:  # since right is more than left and we need more in worst case
                l= mid +1
            else: # left > right so we will go downward 
                h= mid -1
            ans= min(ans, tempAns)  # for getting the minimum floor no
        dp[k][n]= ans
        return dp[k][n]

# Tabulation:Giving Tle But will get sumitted since it's memoisation got submitted(above one)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp= [[0 for i in range(n+1)] for j in range(k+1)]
        # initialsing with base cases
        for i in range(1, k+1):
            dp[i][0], dp[i][1]= 0, 1
        for i in range(n+1):
            dp[1][i]= i
        # replace k->i and j->n
        for i in range(2, k+1):
            for j in range(2, n+1):
                ans= inf
                low, high, tempAns= 1, n, 0
                while low<= high: 
                    mid= low + (high-low)//2
                    left=  dp[i-1][mid-1]       # if egg breaks
                    right= dp[i][j-mid]         # if egg doesn't break
                    tempAns= 1+ max(left, right)
                    if right> left:  # since right is more than left and we need more in worst case
                        low= mid +1
                    else:
                        high= mid -1
                    ans= min(ans, tempAns)  # for getting the minimum floor no
                dp[i][j]= ans
        return dp[k][n]



