# i am not getting the meansing of 'sorted increasing order".

# logic: FOR 1st letter no choice, so put the 1st letter in 'permuatation' before calling the function.
# Now for every 1st letter in remaining string we have two choices i.e 1) add with space 2) Add without spce.

# note: we have to print in increasing order so we will 1st call the function "with space" 
# because "space" has lower ascii value than characters.

# time= O(2 ^(n-1) * n)
class Solution:
    def permutation (self, S):
        
        def solve(per, s):
            if not s:
                ans.append(per)
                return
            solve(per+ " " + s[0] ,  s[1: ])
            solve(per + s[0], s[1: ])
            
        ans= []
        per= S[0]
        solve(per, S[1: ]) 
        return ans


# taking ans inside the function only