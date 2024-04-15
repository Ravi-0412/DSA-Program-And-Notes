# my approach: TLE
# Due to: choice1 = self.minDays(n-1)
# So somehow we have to avoid 'decrement operation by 1'
# Time: O(n)
class Solution:
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n== 0:
            return 0
        choice1, choice2, choice3 = float('inf'), float('inf'), float('inf')
        choice1 = self.minDays(n-1)
        if n % 2 == 0:
            choice2 = self.minDays(n//2)
        if n % 3 == 0:
            choice2 = self.minDays(n - 2*(n//3))
        return 1 + min(choice1, choice2, choice3)
    
# Optimisation
# We have to avoid recursion call when we will take '1' 
# And if we eat only '1' orange then for 'n' orange , it will take 'n' days.

# so for f(n): 
# choice1 = n , eat one orange daily
# choice2 = 1+ (n%2) + f(n/2), 1st make divisible by '2' by eating one single day so 'n% 2' and then eat half so adding '1'
# choice3 = 1+ (n%3) + f(n/3), 1st make divisible by '3' by eating one single day so 'n% 3' and then eat 2/3rd  so adding '1'
# Note: '1' : for operation that will be do by either '2' or '3' after making 'n' divisible by '2' or '3'.

# Time: O(log^2N)

class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 2:
            return n
        option1 = n  # eat one by one
        option2 = 1 + (n % 2) + self.minDays(n//2)
        option3 = 1 + (n % 3) + self.minDays(n//3)
        return min(option1, option2, option3)  

