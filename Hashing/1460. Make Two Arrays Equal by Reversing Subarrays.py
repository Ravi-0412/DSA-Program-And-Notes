# Logic:
"""
kitne bhi size ka subarray ko reverse kar sakte h.
iska matlab agar har element ka frequency same h dono array me then, dono ko equal bna sakte h.
"""

# Time= space = O(n)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count1 = Counter(target)
        for num in arr:
            if count1[num] <= 0:
                return False
            count1[num] -= 1
        return True
        