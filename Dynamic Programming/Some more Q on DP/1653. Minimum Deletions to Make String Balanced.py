# Question meaning: "basically saying that no 'b' can come before any 'a' in a balanced string"
"""
Basic intitution:
At any index, what is the cost of removing all succeeding a's and all preceding b's?
"""

# Method 1: 
# Time = space = O(n)
"""
Approach 1: Three passes with space O(n)
In the first pass, we compute vector "b" which stores the count of character 'b'.
In the second pass, we compute vector "a" which stores the count of character 'a'.
In the third pass, we iterate through the string s.
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a = [0] * n
        b = [0] * n
        
        # Step 1: Count number of 'b's before each index
        c = 0
        for i in range(n):
            b[i] = c
            if s[i] == 'b':
                c += 1
        
        # Step 2: Count number of 'a's after each index
        c = 0
        for i in range(n-1, -1, -1):
            a[i] = c
            if s[i] == 'a':
                c += 1
        
        # Step 3: Find the minimum of a[i] + b[i]
        ans = n
        for i in range(n):
            ans = min(ans, a[i] + b[i])
        
        return ans


# Method 2: 
"""
Two passes with space O(n)
We compute vector a, and instead of computing vector b, we do the processing while iterating through the string itself.
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a = [0] * n
        c = 0
        
        # Step 1: Count number of 'a's after each index (from right to left)
        for i in range(n-1, -1, -1):
            a[i] = c
            if s[i] == 'a':
                c += 1
        
        # Step 2: Calculate the minimum deletions
        ans = n
        c = 0
        
        for i in range(n):
            ans = min(a[i] + c, ans)
            if s[i] == 'b':
                c += 1
        
        return ans


# Method 3:
"""
Two passes with space O(1).
Instead of using vector a and b, we use two variables count_a and count_b.
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Get the count of 'a's in the first pass
        count_a = 0
        for i in range(n):
            if s[i] == 'a':
                count_a += 1
        
        count_b = 0
        ans = n
        
        # Step 2: Iterate through the string and count 'b's
        for i in range(n):
            if s[i] == 'a':
                count_a -= 1
            ans = min(ans, count_a + count_b)
            if s[i] == 'b':
                count_b += 1
        
        return ans

# Method 4: DP
# space = O(n)

class Solution:
    def minimumDeletions(self, s: str) -> int:
        l = len(s)
        # dp stores the number of chars to remove to make s[0:i] valid
        dp = [0] * (l + 1)
        bCount = 0

        for i in range(l):
            if s[i] == 'a':
                # Case 1: Keep current 'a'. Need to remove all 'b's before i, which is bcount.
                # Case 2: Remove current 'a'. Need to remove the current 'a' and whatever makes substring before current i valid, which is dp[i].
                dp[i + 1] = min(bCount, dp[i] + 1)
            else:
                # It's always valid to append 'b' if the substring before i is valid, so just copy dp[i].
                dp[i + 1] = dp[i]
                bCount += 1

        return dp[l]

# Method 5: 
# Optiming space to O(1)
# Since for evaluating current index , we only need to bother about previous index answer.
class Solution:
    def minimumDeletions(self, s: str) -> int:
        cntb = 0
        res = 0
        for x in s:
            if x == 'a':
                res = min(res + 1, cntb)
            elif x == 'b':
                 # Fine for 'b' in the tail
                cntb += 1
        return res

# Similar Q:
# 1)926. Flip String to Monotone Increasing
