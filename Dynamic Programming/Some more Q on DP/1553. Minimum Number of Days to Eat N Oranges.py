# Note: it does not make sense to eat oranges one by one for optimal ans.
# so we have to avoid this step as much as possible.

# Logic for doing 1+ min( (n%2) + f(n/2), (n%3) + f(n/3) ) :
# Since we need to eliminate evaluation of f(n-1), What we do is we only evaluate for n, when n % 2 = 0 or n % 3 = 0. 
# If it is not the case, we simple assume that we took a number of steps, where we ate 1 orange each day.

# Consider a case where n = 2m + 1,
# if we choose to eat 1 orange today, we have even number of oranges left for tomorrow. So we are adding n % 2 for today, when we ate 1 orange.

# On a similar ground we are adding n % 3 to the other option and evaluating only cases when n % 2 =0 or n % 3 = 0.

# for space complexity:
# Another important thing to note is that we are not using an array of size n (or n +1) as in a classic DP problem. 
# This is because we would be storing f(x) only for some values of x, not all. 
# So our array would be sparse and there would be wastage of space (leading to MLE). 
# Instead we can use a map and reduce the amount of space required.

# Time: O(log^2N)

class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 2:
            return n
        return 1 + min((n % 2) + self.minDays(n//2) , (n % 3) + self.minDays(n//3))   # remaining oranges after eating : (n//2), (n//3)


# my approach: TLE
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
        