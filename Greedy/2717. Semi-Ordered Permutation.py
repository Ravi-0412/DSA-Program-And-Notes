# time: o(n)
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n= len(nums)
        i1= nums.index(1)   # index of '1' 
        i2= nums.index(n)   # index of 'n'
        if i2 > i1 :
            # then ans= Bringing '1' to index '0' + Bringing 'n' to index 'n-1'
            return i1 + (n -1 - i2)
        # either bring i1 to index '0' then bring 'n' to index 'n-1' but while bringing '1' to index '0' 'n' will move one step right so '-1' more and same if we bring first 'n' to 'n-1'....our ans will be minimum of both
        return min(i1 + (n- 1 - i2 -1), (n -1 - i2) + (i1 -1))
    