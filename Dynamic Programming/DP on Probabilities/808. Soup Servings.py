# Have to understand properly why it will tend to '1' when n > 4800(even n > 3300).
# watch this after 10:30: https://www.youtube.com/watch?v=XNLJS-uDIqU

# Time = space= O(n^2)
# n= 10^9 but it will get accepted because we will return '1' when n > 3300.

class Solution:
    def soupServings(self, n: int) -> float:

        @lru_cache(None)
        def dfs(a , b):
            # if both becomes empty simultaneously
            if a <= 0 and b <= 0:
                return 0.5
            # if b is empty
            if b <= 0 :
                return 0
            # if 'a' is empty
            if a <= 0 :
                return 1
            # Add all possible choices probability
            return 0.25 *(dfs(a - 100, b) + dfs(a - 75, b- 25) +  dfs(a - 50, b -50) + dfs(a - 25, b - 75))

        return 1 if n > 3300 else dfs(n, n)

