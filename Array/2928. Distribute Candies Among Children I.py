# Method 1: 
# Recursion  + memoisation

# Time : O(n * 3* limit)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        @lru_cache(None)
        def dp(n, c):  # No of ways to distribute 'n' candies among 'c' children.
            if n == 0 :
                # if 'c' == 0, it means we have distributed all candies properly so return 1
                # if c > 0 then give all '0' candies and this is also '1' way
                # if c < 0 then there is no way so return '0'
                return c >= 0
            if n < 0 or c == 0:
                # If n < 0 then there is no way irespectivee of no of children.
                # if c == 0 then from condition till now n > 0 so there is no way
                return 0
            # from here it will execute for n > 0 and  c > 0.
            ans = 0
            for l in range(limit + 1):
                ans += dp(n - l, c - 1)
            return ans
                
        
        return dp(n, 3) 

# Methods without dp and easier one

# Method 2: 
# Brute force using loop

# Time : O(n^3)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        # when sum of candies given to all 3 children = n
                        ans += 1
        return ans


# Method 3:
# Using two loops.

# Logic: Distribute to first two children and then check remaining one is valid distribution for 3rd or not.

# Time : O(n^2)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit) + 1):  # 1st children can get in this range
            # After giving candies to 1st , 2nd children can get in this range
            for j in range(min(n - i, limit) + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    # if candies given to 3rd valid means distribution is correct so incr by '1'.
                    ans += 1
        return ans


# Method 4: 
# Most optimised

# Time: O(n)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        firstMin = max(0, n - 2*limit)  # give other two 'limit' no of candies but 'first' can't get less than '0' candy
        firstMax = min(n, limit)         # give other two zero candies but can't 'first' can't get more than 'l' candies
        # Traverse in range of first and find the possible no of ways for remaining candies among '2'.
        for i in range(firstMin, firstMax + 1):
            # After giving 'i' to 1st , we are left with 'n-i'
            secondMin = max(0, n - i - limit) # give 'limit' no of candies to 3rd from remaining 'n-i'.
            secondMax = min(n-i , limit)      # give 3rd  zero candy from remaining 'n-i'.
            # We have now 'secondMax - secondMin + 1' ways i.e range in which we can give candy to 2nd.
            # No need to worry about 3rd person, once we allocate to first and second the remaining will automatically given to third one.
            ans += secondMax - secondMin + 1
        return ans


# Try to understand O(1) approach using maths
# https://leetcode.com/problems/distribute-candies-among-children-ii/solutions/4276868/100-beat-o-1-detail-explanation-combination-simple-and-easy/