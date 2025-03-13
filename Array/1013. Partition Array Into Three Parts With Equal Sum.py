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

# Method 2: 
"""
Logic: 
Staring from the two ends of the input array, accumulate left and right parts till getting the average values;
If found average values on both parts before the two pointers meet, return true; otherwise, return false.
"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        l, r, s = 1, len(A) - 2, sum(A)
        if s % 3 != 0:
            return False
        leftSum, rightSum, average = A[0], A[-1], s // 3
        while l < r:
            if l < r and leftSum != average:
                leftSum += A[l]
                l += 1
            if l < r and rightSum != average:
                rightSum += A[r]
                r -= 1
            if leftSum == average == rightSum:
                return True    
        return False
