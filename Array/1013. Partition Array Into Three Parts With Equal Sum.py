"""
Just update the no of parts with equal sum seen.
"""

# time: O(n), space = O(1)

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        reqSum = total // 3
        partsSum , partsCount = 0, 0
        for num in arr:
            partsSum += num
            if partsSum == reqSum:
                partsSum = 0
                partsCount += 1
        return partsCount >= 3     # '>=' to handle the case like [0,0,0,0]
