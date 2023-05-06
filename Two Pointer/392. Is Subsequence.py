# logic: traverse both simultaneoulsy and when both char is same incr both pointer else incr pointer of 't' only(say 'j').

# 'i' will tell the no of char of 's' that we seen in 't' at any point of time.

# At last if value of 'i' >= len(s) means we have got all char of 's' in 't'.

# time: O(m + n)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j= 0, 0  # will point to 's' and 't' respectively
        while i < len(s) and j < len(t):
            if s[i]== t[j] :
                i+= 1
                j+= 1
            else:
                j+= 1 
        return i== len(s)  # means we have got all char of 's' in 't'.
