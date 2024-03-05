# exactly same as "22. generate valid parantheis"

# In above Q: No of '(' will be always >= no of ')'.

# Just replace '(' -> 1 and ')' -> 0.

# Q: we have to fill 'n' boxes in such a way that no of '1' is >= no of '0' for all prefix.
# logic in Q: "22. generate valid parantheis"

class Solution:
    def NBitBinary(self, N):
        ans= []
        
        def AllNumber(noOne, noZero, number):
            if noOne + noZero== N:
                ans.append(number)
                return
            if noOne < N:
                AllNumber(noOne + 1, noZero, number + "1")
            if noZero < noOne:
                AllNumber(noOne , noZero + 1, number + "0")
        
        AllNumber(0,0,"")  # (noOne, noZero, number)
        return ans
    
