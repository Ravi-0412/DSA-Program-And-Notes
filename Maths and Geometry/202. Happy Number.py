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
