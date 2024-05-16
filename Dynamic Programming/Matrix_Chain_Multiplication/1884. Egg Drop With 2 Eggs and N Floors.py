# 1) suppose if egg= 1 and no of floor== 'n'.
# logic:
# just start dropping egg from floor 1 and if breaks then required floor is '0' 
# and if doesn't break go on checking for next floor. But this will only work if we were given one egg only.
# In this way we may need to go till 'n' floor.
# so ans = n(remaining floor).

# If no of eggs will increase then no of moves will decrease.

# Note vvvi:The problem is not actually to find the critical floor, 
# but merely to decide floors from which eggs should be dropped so that the total number of trials is minimized.
# Sequence of floors from which we drop the egg.

# Note: Egg ko bhi bacha ke rakhna h taki hm exact floor find kar paye.

# Now coming to this Q(egg = 2)
# say no_of_floor(f) = 100

# Method 1: Binary search.
# we start from the 50’th floor, then we end up doing 50 comparisons in the worst case.
# The worst-case happens when the required floor is 49’th floor. 

# How?
# if start to drop from 50th floor if it breaks then, we need to check all floor from '1' to '49' one by one
# since no of remaining egg = 1 (case : 1)

# Method 2: Optimised one:
# Let us make our first attempt on x'th floor. 
# Ye man ki 'x' no se jyada trial nhi le sakte kyonki agar egg break ho gya tb one by one check karna hoga (1 to x-1).

# If it breaks, we try remaining (x-1) floors one by one. 
# So in worst case, we make x trials.

# If it doesn't break, we jump (x-1) floors (Because we have
# already made one attempt and we don't want to go beyond 
# x attempts.  Therefore (x-1) attempts are available),
#     Next floor we try is floor x + (x-1)

# Similarly, if this drop does not break, next need to jump 
# up to floor x + (x-1) + (x-2), then x + (x-1) + (x-2) + (x-3)
# and so on.

# Since the last floor to be tried is 100'th floor, sum of
# series should be 100 for optimal value of x.

#  x + (x-1) + (x-2) + (x-3) + .... + 1  = 100

#  x(x+1)/2  = 100
#          x = 13.651

# How minimum 14 moves?
# One optimal strategy is: (See leetcode example explanation

# OR
# we start trying from 14'th floor. If Egg breaks on 14th floor
# we one by one try remaining 13 floors, starting from 1st floor.  If egg doesn't break
# we go to 27th floor.
# If egg breaks on 27'th floor, we try floors form 15 to 26.
# If egg doesn't break on 27'th floor, we go to 39'th floor.

# An so on...

# Ans link : https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/


# Note : This we can generalise for 'n' floors.

# Note vvi: we can only find the minimum no of moves required to find the exact floor but we can't find the exact floor
# by this approach. Finding exact floor will be very difficult.

# Note vvi:  we want the worst possible case between the two sub-problems. 
# And the overall answer is the best (min) of the worst (max) cases.

# Note vvi: Here for no fo eggs = 2 no of moves(our ans) will be also equal to the threshhold floor(above which egg will drop for sure)

# Time : O(root(n))

class Solution:
    def twoEggDrop(self, n: int) -> int:
        i = 1
        while (i * (i + 1))/ 2 < n:
            i += 1
        return i


# Method 3: Dynamic Programming
# Note vvi: we want the worst possible case between the two sub-problems.(when it breaks and when it doesn't break)
# And the overall answer is the best (min) of the worst (max) cases.

# Just the conversion of above observations.

# Logic: Just trying to drop from floors which can minimize our ans i.e 
# finding the sequence of floors from which we can drop.
# So try each possibility i.e drop from each floor.

# Time : O(n^2)

class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp= [-1 for i in range(n+1)]
        return self.f(n, dp)  
    
    def f(self, n, dp):  # will give minimum nof of moves when no of floor is 'n'.
        if n <= 1:  
            return n
        if dp[n]!= -1:
            return dp[n]
        # now check from each floor one by one
        ans= float('inf')
        for i in range(1, n + 1):
            # 1) if break then check all floor from '1' to 'i-1' => i -1 moves
            # 2) If it doesn't break then check the remaining floor i.e 'n- i'
            tempAns= 1+ max(i -1, self.f(n-i, dp))
            ans= min(ans, tempAns) 
        dp[n]= ans
        return dp[n]


# Extension of this Q: "887. Super Egg Drop".
