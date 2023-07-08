# Logic: store in set to do 'add' and 'remove' in O(1).
# moveFrom : means marbles won't be at this position, so remove this position
# moveTo :   means marble will come at this position, so add this position

# At last return the sorted list.

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        numSet= set(nums)
        for i in range(len(moveFrom)):
            numSet.remove(moveFrom[i])
            numSet.add(moveTo[i])
        ans = list(numSet)
        ans.sort()
        return ans
        
        