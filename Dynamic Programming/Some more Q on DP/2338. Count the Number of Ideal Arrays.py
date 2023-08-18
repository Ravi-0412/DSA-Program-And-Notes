# Logic: our sequence can start from any number, So start with any number.
# We need to keep track of last included no to know next number we can include and 
# we also need to keep tarck of no of ele included till now.

# Note: best apply mod while you are returning only to avoid confusion about 'mod'.

# subproblems will repeat like [1,1,2] and [1,2,2](array till now) both can call next function for (4, 3) and so on.

# Recursion  + memoisation
# Time : O(n^2 *logn) = TLE

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def solve(cur, eleIncluded):
            if eleIncluded == n:
                return 1
            ans = 0
            j = 1
            while cur * j <= maxValue:
                ans += solve(cur * j, eleIncluded + 1)
                j += 1
            return ans % mod
        
        ans = 0
        for i in range(1, maxValue + 1):
            ans += solve(i, 1)
        return ans % mod
    
# for calling the function one by one, i was doing like this.
# will give error.
ans = 0
for i in range(1, maxValue + 1):
    ans += solve(i, 1)
    return ans % mod


# Note vvi: whenever you get TLE by actual approach of DP or anywhere 
# Just try to find any pattern or try to find any mathematical logic.

# Optimising the above solution
# We can avoid adding the same element to our subarray i.e we will calculate ans for strictly increasing subarray and
# from that we can find ans if are allowed to take that much ele (repitition allowed) then what will be the ans.

# gen(k): computes number of valid arrays from k numbers of length 'n'.
# This we can get from 'stars and bars' logic.
# Read this with proof: https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)#Theorem_one_proof

# 'stars and bars' logic:
# 1) For any pair of positive integers n and k, the number of k-tuples of positive integers whose sum is n is equal to ?
# i.e x1 + x2 + x3 ..xk = n (x1,x2...> 0)
# Ans: (n-1 , k-1) i.e (n-1) choose (k-1).

# Proof: start by placing the stars in a line
# There are n − 1 gaps between stars. A configuration is obtained by choosing k − 1 of these gaps to contain a bar; 
# therefore there are (n-1) choose (k-1) possible combinations.

# 2) if x1 + x2 + x3 ..xk = n (x1,x2...>=0) i.e the number of k-tuples of non-negative integers whose sum is n is equal to ?
# Ans : (n - 1 + k, k -1) i.e (n-1 + k) choose (k-1).

# Proof : Read above link.

# Note: Theorem 1 can now be restated in terms of Theorem 2, 
# because the requirement that all the variables are positive is equivalent to pre-assigning each variable a 1, 
# and asking for the number of solutions when each variable is non-negative.

# For example:
# n = 10, k= 4
# x1 + x2 + x3 + x4 = 10 (x1,x2,x3..> 0) is equivalent to : x1 + x2 + x3 + x4 = 6 (x1,x2,x3.. >= 0).

# How this can help in optimisation?
# Take a strictly increasing ideal array of length len1, we can repeat numbers in the array to create an ideal array of longer length len2. 
# For example, from [1, 2, 4], we can get [1,1,1,2,4], [1,1,2,2,4],[1,2,4,4,4], ...

# for generating the ideal array of len2 from array of length 1, we can use 'stars and bars logic'.

# But how?
# For example, we want to translate a strictly increasing array [1,2,4] of length 3 into an ideal array of length 5, 
# then we need to decide how many 1s to fill, how many 2s to fill, and how many 4s to fill in the ideal array.

# Steps :
# 1) ideal array: _ _ _ _ _ (5 positions to fill)
# 2) We can split it into 3 subarrays by putting 2 bars between any positions. Some valid ways to split:
# _ | _ | _ _ _ (this translates to 1 | 2 | 4 4 4 )
# _ _ | _ | _ _ (this translates to 1 1 | 2 | 4 4 )

# 3) This is essentially choosing 2 from 4 (2 bars to place, 4 potential places to put the bars)

# Generalising:
# N = The number of ways to create a ideal array of length len2 from a strictly increasing ideal array of length len1
# N = nChooseK(len2 - 1, len1 - 1)
# There are len2 - 1 of potential places to put the bars
# There are len1 - 1 bars to place.

# Which is just same as 'stars and bars' method.

# Why the length of strictly increasing ideal array is at most 14?
# Note that 2^14 > 10,000, so the longest striclty increasing ideal array is:
# [1, 2, 4, 8, ..., 8096] or
# [2^0, 2^1, 2^2, ..., 2^13]

# Read this solution with above wikipedia link for more clarity:
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2262093/java-passed-understandable-solution-will-illustration-solving-strictly-increasing-case-first/


# Note: using this there is no need to start checking from same ele for next ele we can start to check from next possible ele.

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        mod = 10**9 + 7
        
        @lru_cache(None)
        def gen(k):            
            return math.comb(n-1, k-1)

        @lru_cache(None)
        def dp(cur, l):
            # just add the ans. number of ways to create a ideal array of length 'n' from a strictly increasing ideal array of length 'l'.
            res = gen(l)  
            nxt = cur * 2  # start checking from next number.
            if l == n or nxt > maxValue:
                # then simply return res from here 
                return res
            while nxt <= maxValue:
                res += dp(nxt, l+1)
                nxt += cur
            return res % mod
                
        ans = 0
        for i in range(1, maxValue + 1):
            ans += dp(i, 1)
        return ans % mod


# Later try by this approach also.
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2261280/python-arranging-primes-intro-to-combinatorics/