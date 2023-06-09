#logic: Give a number x (string), we construct a new string with the same length digit by digit from the most significant digit.

# How to solve Digit DP problems?
# 1)
# tight: will tell whether my bounds are tight or not i.e what's the range of integer i can place at cur index.
# if tight means tight == 1 means we have to take care of digits we are placing i.e we can only place the digit <= num at that index.
# if not tight then we can place any number between '0-9'.

# in this way we can generate all the numbers .
# Note vvi: Number generated will be less than 'n' because of tight variable.

# Now we have to check the validity.
# and for checking their validity , for this Q
# we will pass sum of digits till now we have taken also in function with (index, tight).
# And when you reach at last of string check whether sum lies in the given range or not.


# Time complexity: O(num2.length() * 2*  min(num2.length() * 9, max_sum) ) i.e= ind * tight * curSum
# Space complexity: O(min(num2.length() * 9, max_sum))


# generalised version

# nOte: Number generated will be always less than 'n'. 
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        s= ""
        mod= 10 ** 9 + 7
        
        @lru_cache(None)
        # gives the no of valid numbers from cur index to last for given bound and given curSum.
        def solve(ind, tight, curSum):
            if ind== len(s):
                # means we have placed digits at all places of having length= s
                if curSum >= min_sum and curSum <= max_sum:
                    return 1
                return 0
            ans= 0
            # find if bound is tight for cur index or not.
            end= int(s[ind]) if tight else 9  # if tight we can place only digit which is <= num at s[ind] else we can place 0-9.
            # now start placing the possible digit i.e from '0' to end
            for digit in range(end + 1):
                newSum = curSum + digit
                newTight= tight and digit == end  # if bound is already tight for cur index and if we have placed the 
                                                # max possible num at cur index then bound will be tight for next index
                # sbka ans ko add kar do
                ans += solve(ind + 1, newTight, newSum)
                ans %= mod
            return ans
        
        s= num2   
        # first finding the count of valid numbers from [0, num2]
        ans= solve(0, 1, 0)  # for the 1st call bound will be always tight because at the 1st place
                             # we are boun dto place the digit which is less than the 1st digit of given number.
        # now find the count of valid numbers from [0, num1 -1] 
        # and subtarct this from above i.e [0, num2] to get no of valid numbers from [num1, num2]
        
        solve.cache_clear()   # clear the dp states for new call
        s= str(int(num1) -1)   
        ans -= solve(0, 1, 0)   # all generated num will be less than 'num1'
        return ans % mod
    
# improving little bit 
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        s= ""
        mod= 10 ** 9 + 7
        
        @lru_cache(None)
        def solve(ind, tight, curSum):
            if ind== len(s):
                # means we have placed digits at all places of having length= s
                if curSum >= min_sum and curSum <= max_sum:
                    return 1
                return 0
            ans= 0
            # find if bound is tight for cur index or not.
            end= int(s[ind]) if tight else 9  # if tight we can place only digit which is <= num at s[ind] else we can place 0-9.
            # now start placing the possible digit i.e from '0' to end
            for digit in range(end + 1):
                newSum = curSum + digit
                if newSum > max_sum:  # next digits are more greater than curr so newSum always greater
                    break
                newTight= tight and digit == end  # if bound is already tight for cur index and if we have placed the 
                                                # max possible num at cur index then bound will be tight for next index
                ans += solve(ind + 1, newTight, newSum)
                ans %= mod
            return ans
        
        s= num2
        # first finding the count of valid numbers from [0, num2]
        ans= solve(0, 1, 0)  # for the 1st call bound will be always tight because at the 1st place
                             # we are boun dto place the digit which is less than the 1st digit of given number.
        # now find the count of valid numbers from [0, num1 -1] 
        # and subtarct this from above i.e [0, num2] to get no of valid numbers from [num1, num2]
        
        solve.cache_clear()   # clear the dp states for new call
        s= str(int(num1) -1)
        ans -= solve(0, 1, 0)
        return ans % mod
                

# in above method since we are already neglecting the higher sum in for loop then we only need to check if curSum < min_sum.
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        s= ""
        mod= 10 ** 9 + 7
        
        @lru_cache(None)
        def solve(ind, tight, curSum):
            if ind== len(s):
                # means we have placed digits at all places of having length= s
                if curSum < min_sum:
                    return 0
                return 1
            ans= 0
            # find if bound is tight for cur index or not.
            end= int(s[ind]) if tight else 9  # if tight we can place only digit which is <= num at s[ind] else we can place 0-9.
            # now start placing the possible digit i.e from '0' to end
            for digit in range(end + 1):
                newSum = curSum + digit
                if newSum > max_sum:  # next digits are more greater than curr so newSum always greater
                    break
                newTight= tight and digit == end  # if bound is already tight for cur index and if we have placed the 
                                                # max possible num at cur index then bound will be tight for next index
                ans += solve(ind + 1, newTight, newSum)
                ans %= mod
            return ans
        
        s= num2
        # first finding the count of valid numbers from [0, num2]
        ans= solve(0, 1, 0)  # for the 1st call bound will be always tight because at the 1st place
                             # we are boun dto place the digit which is less than the 1st digit of given number.
        # now find the count of valid numbers from [0, num1 -1] 
        # and subtarct this from above i.e [0, num2] to get no of valid numbers from [num1, num2]
        
        solve.cache_clear()   # clear the dp states for new call
        s= str(int(num1) -1)
        ans -= solve(0, 1, 0)
        return ans % mod
                



                

                

                

