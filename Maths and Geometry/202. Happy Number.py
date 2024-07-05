# Time :  O(logN) where N is the number.
# Space : O(logN)

# Logic: just we are checking if we are getting same number then there is cycle.
class Solution:
    def isHappy(self, n: int) -> bool:
        visited= set()
        while n not in visited:  # stopping condition means no can't be happy
            visited.add(n)
            n= self.sumOfsquare(n)
            if n== 1:
                return True
        return False
    
    def sumOfsquare(self, n):
        ans= 0
        while n:
            remainder= n % 10
            ans+= remainder * remainder
            n= n//10
        return ans


# Method 2: 
# In linear space

# Logic: the non-happy number will repeat itself.
# suppose the non-happy number does not repeat it self, the code will stuck in infinite loop and we will never get result back.

# So just we are checking if there is cycle while replacing number with square of sum. 
# If there is cycle then we can check cycle value, if it = 1 then happy else non-happy.

# For detecting cycle, we can use logic of 'detecting cycle' in a linklist i.e 'Floyd Cycle detection algorithm'.

# space : O(1)

class Solution:
    def isHappy(self, n: int) -> bool:

        # Just giving 'sumOfSquareOfDigit(n)'
        def next(n):
            next_no = 0
            while n:
                r = n % 10
                next_no += r *r
                n //= 10
            return next_no
        
        slow = n
        fast = next(n)
        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return slow == 1
        