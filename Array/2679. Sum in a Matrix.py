# method 1: Brute force 
# simply did what they are telling to do.

# time: O(n^2)

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        r, c= len(nums), len( nums[0])
        count= r*c
        ans= 0
        while count >0:
            mx= float('-inf')
            for i in range(r):
                max_row= max(nums[i])
                mx= max(mx, max_row)
                nums[i].remove(max_row)
            count-= r
            ans+= mx
        return ans


# method 2:
# time: O(n^2)
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
