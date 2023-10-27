# Just an extension of "2262. Total Appeal of A String"

# Read Q properly(see the example properly)
# 'Unique char' means here char which has no duplicate.
# e.g : aba , no of unique char acc to Q = 1 only i.e 'b' because 'a' has its duplicate present.

# Note: when we add any ele to already existing one then 
# then no of new substring we get = len(after adding cur char).

# e.g: pre = "ab", and say cur_char = c then, no of new substring
# equal = 3 i.e len(abc) . 'abc' , 'bc' , 'c'. 

# When we will add any cur char then it will not make any impact with those substring before index
# when it was seen second last time.

# for cur index 'i' to last_seen , it will form unique substring so we will add these substring
# And from index 'last_seen' to 'second_last_seen' it will become duplicate so count will decrease for these substring.


# Time = space = O(n)

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dp = [0]* (len(s) + 1)   # dp[i] will store the sum of unique_char in all unique substring that got generated after adding s[i]
        last_seen = [-1] * 26     # when last time s[i] was seen
        second_last_seen  = [-1]*26  # second_last_time s[i] was seen
        for i, c in enumerate(s):
            ind = ord(c) - ord('A')
            last , second_last = last_seen[ind] , second_last_seen[ind]
            # number of substrings where s[i] was unique in the substring, but now it no longer unique
            # so we have to remove all those substring
            sub_removed = last - second_last   # s[i] was unique before , but it will be duplicate for this much substring
            # Number of substring where s[i] is unique, we have to add all these substring
            sub_added = i - last  # s[i] will be unique for this much substring.
            dp[i + 1] = dp[i] + sub_added - sub_removed
            second_last_seen[ind] = last_seen[ind]
            last_seen[ind] = i
        return sum(dp)
