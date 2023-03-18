# if egg= 1 and no of floor== 'n'.
# logic:
# just start dropping egg from floor 1 for better utilisation of given egg and if breaks then required floor is '0' (1-0) 
# and if doesn't break go on checking for next floor. But this will only work if we were given one egg only. 

# just same as "375. Guess Number Higher or Lower II".
# logic: ans will depend on from which floor we start checking for remaining egg and remaining floor to check.
# we can start checking from any floor. There will be two condition:
#  1) egg brakes on 'i'th floor. then call the function with one less egg and one less floor i.e f(k-1, i-1). floor must be less than the curr floor number we checked.
# 2) egg doesn't brake on 'i'th floor. then call the function with one same egg and one more floor i.e f(k, n-i). since floor can be even higher

# note: move will not depend on floor number , it will depend on from which floor we start to check for remaining floor to check.
# vvi: The problem is not actually to find the critical floor, but merely to decide floors from which eggs should be dropped so that the total number of trials is minimized. 


# videos: 
# https://www.youtube.com/watch?v=iOaRjDT0vjc
# Note: we should eggs always greater than '0'.

# we can think like given 'k' eggs and 'n' floor, how many minimum no eggs we have to drop to know the required floor.
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        return self.f(k , n)  # it denotes the min no of moves ,given no of eggs 'k' and remaining floor we have to check is 'n'
    
    def f(self, k, n):
        if n== 0 or n== 1:  # if remaining floor is '0' or '1' then we need '0' or '1' move respectively.
            return n
        if k== 1:  # go on checking floor from 1 to 'n'(in worst case).. this case also means k==1 and (n!=0 or 1)
            return n
        # now check from each floor one by one
        ans= float('inf')
        for i in range(1, n): 
            # if egg break then we need to check till 'i-1' with 'k-1' egg and
            #  if doesn't then remaining floor to check will be 'n-i' with 'k' eggs as we have to find max floor.
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
        ans= float('inf')
        for i in range(1, n):  # can also include 'n' np but base case will handle when remaining floor==1.
            # if egg break then we need to check till 'n-1' with 'k-1' egg and
            #  if doesn't then remaining floor to check will be 'n-i' with 'k' eggs as we have to find max floor
            tempAns= 1+ max(self.f(k-1, i-1, dp), self.f(k, n-i, dp))
            ans= min(ans, tempAns)  # for getting the minimum floor no
        dp[k][n]= ans
        return dp[k][n]



# optimising memoization using bottom up and binary search
# here we find the move for mid floor and then take the decision accordingly.
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
        if n== 0 or n== 1:  # if remaining floor is '0' or '1' then we need '0' or '1' move respectively.
            return n
        if k== 1:  # go on checking floor from 1 to 'n'(in worst case)
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
            left=  self.f(k-1 , mid-1, dp)  # if egg broken check for down floors of mid..
            right= self.f(k , n- mid, dp)   # if egg doesn't break , check for up floors of mid
            tempAns= 1+ max(left, right)     # store max of both 
            if right> left:  # since right is more than left and we need more in worst case
                l= mid +1    # so l=mid+1 to gain more temp for worst case : upward
            else: # left >= right so we will go downward 
                h= mid -1
            ans= min(ans, tempAns)  # store minimum attempts
        dp[k][n]= ans
        return dp[k][n]


# method 2:
# Try to understand this also later.
# https://leetcode.com/problems/super-egg-drop/solutions/443089/simplest-python-dp-solution-with-detailed-explanation-99-time-100-mem/
# https://leetcode.com/problems/super-egg-drop/solutions/158974/c-java-python-2d-and-1d-dp-o-klogn/


