# logic: for digit we have no option i.e just add the digit in the 'permutation'
# And if it is letter then we have two choice 1) consider lower case 2) consider upper case . 
# And we have to take both the option.

# Note: no return statement till we find any ans . so return statement after calling function.

# time: O(2^n)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def solve(s, per):
            if not s:
                ans.append(per)
                return
            if s[0].isdigit():
                solve(s[1: ], per + s[0])
            else:  # if letter
                solve(s[1: ], per + s[0].lower())
                solve(s[1: ], per + s[0].upper())
        
        ans= []      
        solve(s, "")
        return ans


# taking ans inside function only.
# how to do this?
# Ans: jo tmko return karna h usko base case me return karo and ans ke anusar sb return ko manipuate kar do.
# like here jitna bhi 'per' milega sbko add kar dena h ans me.
# ilsiye sb jahan 'ans+= f()'  and last me ans ko return kar do.
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def solve(s, per):
            ans= []
            if not s:
                return [per]
            if s[0].isdigit():
                ans+= solve(s[1: ], per + s[0])
            else:
                ans+= solve(s[1: ], per + s[0].lower())
                ans+= solve(s[1: ], per + s[0].upper())
            return ans
         
        return solve(s, "")
