# Logic:
"""
just same as :"1151. Minimum Swaps to Group All 1's Together' except this is circular.
how to handle circular case?
=> if subarray starts from last index then it will need 'k-1' element from start to checking.
where k = total_no_one.
for this just append first 'k-1' element into data at last and apply same logic as '"1151. Minimum Swaps to Group All 1's Together'.
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount = 0
        for num in data:
            if num == 1:
                oneCount += 1
        for i in range(oneCount - 1):
            data.append(data[i])
        n = len(data)
        i, j = 0, 0
        zeroCount = 0
        ans = oneCount
        while j < n:
            if data[j] == 0:
                zeroCount += 1
            if j + 1 >= oneCount:
                ans = min(ans, zeroCount)
                if data[i] == 0:
                    zeroCount -= 1
                i += 1
            j += 1
        return ans
