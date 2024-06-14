# Logic: Just find the first two minimum and its sum.

# time: O(n)

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        firstMin, secondMin = 10**5 + 1, 10**5 + 1 
        for num in prices:
            if num < firstMin:
                secondMin = firstMin
                firstMin = num
            elif num < secondMin:
                secondMin = num
        return money if firstMin + secondMin > money else money - (firstMin + secondMin)