# Method 1: Using dp

# Logic: when we see any vowel at index 'i' then, this can contribute to all substring starting from index '0' to 'i'
# i.e it will add 'i + 1' tp dp[i -1] => dp[i -1] + (i + 1).
# And no vowel at index 'i' then it will continue the pre i.e dp[i -1]

# Time = space = O(n) 
class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        dp = [0] * (n+ 1)
        for i, c in enumerate(word):
            if c in "aeiou":
                dp[i + 1] = dp[i] + (i + 1)
            else:
                dp[i + 1] = dp[i]
        return sum(dp)

# Method 2: 

# we use the fact that each character appears in (i + 1) * (n - i) substrings. 

# How formula '(i + 1) * (n - i)' came?

# Generalisation:
# Let's start with the general formula:
# Step 1 - Every substring has one start point and one end point
# Step 2 - A character can be part of any substring if start of substring is before it and end of substring after it.
# Step 3 - we can have total possible start points = (i + 1)
# Step 4 - we can have total possible end points = (n - i)
# Step 5 - total substring = total possible start point * total possible end point = (i + 1) * (n - i).

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i, c in enumerate(word):
            if c in "aeiou":
                ans += (i + 1) * (n - i)
        return ans