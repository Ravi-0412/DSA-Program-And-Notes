# Intuitive: Similar to backpack DP problem as Leetcode 416. "416. Partition Equal Subset Sum".
# Vvi: But this one is more challenging because some data ele may not be chosen in any of the support.

# My mistake: i had thought in above way only.


# Method 1: Recursion
# Even after applying DP, time complexity= O(n*s*s) , s = sum(rods)
# i.e = O(20 * 5000 * 5000) = O(5 * 10**8) 
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        def solve(i, s1, s2):
            if i == len(rods):
                if s1 == s2:
                    return s1
                return 0
            # 1)  don't include this rod in any of the support
            opt1 = solve(i + 1, s1, s2)
            # 2) Now if we want to include in support then we have two choices:
            # i) Include in support s1 or 
            opt2 = solve(i + 1, s1 + rods[i], s2)
            # ii) include in support s2
            opt3 = solve(i + 1, s1, s2 + rods[i])
            return max(opt1, opt2, opt3)

        return solve(0, 0, 0)    # (index, s1_sum, s2_sum)
    

# How we can optimise the above solution
# Logic: Instead of taking s1 and s2, if we take the difference & if at last difference == 0 then we have found one ans.
# So we can convert (s1, s2) to one state i.e their diff.

# Conversion:
# Range of s1 = 0 <= s1 <=5000
# Range of s2 = 0 <= s2 <=5000
# So Range(difference) = -5000 <=diff <= 5000.

# But when we will do memoisation using dp array then we can't store value at negative index.
# So we can do shifting by '5000' (max negative one) to get +ve index in case of diff.

# So finally our no of states will get reduced i.e 
# Time complexity = O(n*2* s), s= 5000

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        @lru_cache(None)
        def solve(i, diff):
            if i == len(rods):
                if diff == 0:
                    return 0
                return float('-inf')
            # 1)  don't include this rod in any of the support
            opt1 = solve(i + 1, diff)
            # 2) Now if we want to include in support then we have two choices:
            # i) Include in support s1 or 
            opt2 = rods[i] + solve(i + 1, diff + rods[i])
            # ii) include in support s2
            opt3 = solve(i + 1, diff - rods[i])
            return max(opt1, opt2, opt3)

        ans= solve(0, 0)
        if ans < 0:   # it will be float('-inf')
            return 0
        return ans
    

# Memoisation using dp array
# Analyse properly
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        def solve(i, diff):
            if i == len(rods):
                if diff == 0:   # we are already including the ele before only in s1.
                    return 0
                return float('-inf')
            if dp[i][diff] != -1:
                return dp[i][diff]
            # 1)  don't include this rod in any of the support
            opt1 = solve(i + 1, diff)
            # 2) Now if we want to include in support then we have two choices:
            # i) Include in support s1 or .
            # In this case , diff will increase by 'rods[i]'. and adding 'rod[i]' at first to get the maximum height.
            opt2 = rods[i] + solve(i + 1, diff + rods[i])
            # ii) include in support s2. Diff will decrease.
            # But we are not adding 'rods[i]' at first like 'opt1' because 
            # if we add here also then that ele will get added two times in our ans.
            opt3 = solve(i + 1, diff - rods[i])
            dp[i][diff] = max(opt1, opt2, opt3)
            return dp[i][diff]

        n = len(rods)
        offset = 5000
        dp = [[-1 for sum in range(2 * offset + 1)] for i in range(20 + 1)]
        ans= solve(0, 0)
        if ans < 0:   # it will be float('-inf')
            return 0
        return ans

# Other medthods:(after 3rd link in sheet)
# Try to understand those also.
# https://leetcode.com/problems/tallest-billboard/solutions/203261/java-knapsack-o-n-sum/
# https://leetcode.com/problems/tallest-billboard/solutions/203181/java-c-python-dp-min-o-sn-2-o-3-n-2-n/
