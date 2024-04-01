class Solution:
    def maxBottlesDrunk(self, bottles: int, exchange: int) -> int:
        ans = bottles
        empty = bottles
        while empty >= exchange:
            empty -= exchange
            exchange += 1
            ans += 1
            empty += 1
        return ans
