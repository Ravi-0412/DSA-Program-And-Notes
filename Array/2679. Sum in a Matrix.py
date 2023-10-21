# Logic: just sort all 1D array.
# Then go column wise and take max ele of that column and add it to ans.
# time: O(r*c*logc)
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        r, c= len(nums), len( nums[0])
        for i in range(r):
            nums[i].sort()
        ans= 0
        for i in range(c):
            mx= float('-inf')
            for j in range(r):
                mx= max(mx, nums[j][i])
            ans+= mx
        return ans
