# Note: when we add any ele to already existing one then 
# then no of new substring we get = len(after adding cur char).

# e.g: pre = "ab", and say cur_char = c then, no of new substring
# equal = 3 i.e len(abc) . 'abc' , 'bc' , 'c'. 

# What is the appeal of all substrings that end at i-th position?

# It is the same as the appeal of all substrings that end at i - 1 position, plus:
# number of substrings (ending at i-th position) that do not contain s[i] character.
# to count those substrings, we just track the previous (prev) position of s[i] character.

# Note: After last seen index of char, cur char won't affect the ans
# i.e after last_seen_index it will generate new substring.

# Just add the new substring and add to prev one (i -1) because dp[pre] has already calculated the sum 
# So we only need to add the effect of cur char i.e
# suppose s = abc and we are currently at index '2' then, 
# new substring that will affect our ans = 3 len(abc) i.e c, bc , abc. 
# dp[pre] = 3  then we only need to add '3' to dp[pre] to get the sum of appeal of all unique substring after adding s[i].

# Why it is working?
# newly generated substring are : c, bc, abc
# But we have alreay calculated the sum for 'b', 'ab' i.e last two one
# we on;y need to add for cur char 'c' and 1 for each other substring where we are adding 'c' i.e 'b', 'ab'.

# time = space = O(n)

class Solution:
    def appealSum(self, s: str) -> int:
        dp = [0]* (len(s) + 1)   # dp[i] will store the sum of appeal of all unique substring after adding s[i]. 
                                # made of 'n + 1' to handle the case for i= 0.
        last_seen = [-1] * 26     # when last time s[i] was seen
        for i, c in enumerate(s):
            ind = ord(c) - ord('a')
            last  = last_seen[ind]
            # so we have to remove all those substring
            # Number of substring where s[i] is unique, we have to add all these substring
            sub_added = i - last  # s[i] will be unique for this much substring.
            dp[i + 1] = dp[i] + sub_added  # 
            last_seen[ind] = i
        return sum(dp)
    

# method 2: 
# Very easy and concise
# we use the fact that each character appears in (i + 1) * (n - i) substrings. 
# However, it does not contribute to the appeal of substrings on the left that already include that character. 
# For example, for string "abcab", the second 'a' character contributes to the appeal of 6 substrings:

# "abca" and "abcab" (first 'a' character is already counted)
# "bca" and "bcab"
# "ca" and "cab"
# "a" and "ab"

# To exclude previously counted substrings, we just track the previous (prev) position of s[i] character. 
# So, the final formula is (i - prev[ch]) * (n - i).

# How formula '(i + 1) * (n - i)' came?

# Generalisation:
# Let's start with the general formula:
# Step 1 - Every substring has one start point and one end point
# Step 2 - A character can be part of any substring if start of substring is before it and end of substring after it.
# Step 3 - we can have total possible start points = (i + 1)
# Step 4 - we can have total possible end points = (n - i)
# Step 5 - total substring = total possible start point * total possible end point = (i + 1) * (n - i).


# Regarding the distinct characters counting:

# We are basically checking each 'characters' contribution to its created substrings.
# If there is a repeating character later on, you will see that the repeating character's
# contribution would be double-counted - if you take all of its substrings contribution.
# Since we want just the distinct character count (and not repeated counts), 
# we count only substrings formed from next index of prev occurred character.


class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        last_seen = [-1] * 26     # when last time s[i] was seen
        ans = 0
        for i, c in enumerate(s):
            ind = ord(c) - ord('a')
            last = last_seen[ind]
            ans += (i - last) * (n - i)
            last_seen[ind] = i
        return ans


# extended version: "828. Count Unique Characters of All Substrings of a Given String".