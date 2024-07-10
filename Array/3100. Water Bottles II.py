# Just same as :"2739. Total Distance Traveled"

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        # Run till we can exchange
        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1
            ans += 1
        return ans

# Method 2:
# in one line
# 'numExchange' empty karne pe '1' bottle mil hi jayega isliye actual me 'numExchange - 1' empty hoga,
# except 1st time(isliye '-1').

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
        