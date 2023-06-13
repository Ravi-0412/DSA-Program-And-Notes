# Explanation:
# a in prefix is good, skip all a in the beginning.
# If all characters are a, change the last char to z.
# From the first char not a, decrese them, until next a.

# time: O(n), space: O(n)

class Solution:
    def smallestString(self, s: str) -> str:
        n= len(s)
        s= list(s)   # we can't change in string so first converting into list.
        i= 0
        # skip all a in the beginning because it is already smallest lexographically till now.
        while i  < n and s[i] == 'a':
            i += 1
        # If all characters are a, change the last char to z. Because we have to perform at exacyly one operation so change the last one.
        # and for 'a' we will change to 'z' only.
        if i == n:
            s[n-1]= 'z'
            return "".join(s)
        # Now to get the smallest we will start decreasing  from first non_a char till we will find next 'a' 
        # because if we include 'a' also then it will become bigger as 'a' will change to 'z'.
        while i < n and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i += 1
        return "".join(s)


# my mistake: I thought excatly same way only but was not able to code.
# Reason: I was trying to find the indexes of first_a, 2nd_a, first_non_a...
# so it become totally difficult.
