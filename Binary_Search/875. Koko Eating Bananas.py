# the lower bound of the search space is 1, and upper bound is max(piles), 
# because Koko can only choose one pile of bananas to eat every hour. 
# so end= max(piles) 
# time: O(log(max(piles)))

# len(piles) <= 'h' then only koko can eat all the bananas. since in one hour she can eat only one pile
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end, n= 1, max(piles), len(piles)
        while start  < end:
            mid= start+ (end-start)//2
            if self.isValid(piles, h, mid):
                end= mid
            else:
                start= mid+ 1
        return start

    # agar koko is speed se khata h then kya 'h' hour me pura banana kha payega? 
    def isValid(self, piles, h, speed):
        hour= 0
        for pile in piles:
            hour+= math.ceil(pile/speed)
        return hour <= h

