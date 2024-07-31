# Method 1:
# Take each element as peak and find number that we can include
# on its left and right && take max.

# Time = space = O(n) and we are doing 3 traversal.

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        up, down = [0] * n , [0]*n
        # finding the no of elements smaller while going up
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i-1] + 1
        # finding the no of elements smaller while coming down
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1
        ans = 0
        for i in range(n):
            if up[i] > 0 and down[i] > 0:
                ans = max(ans, up[i] + down[i] + 1) 
        return ans

# Method 2:
# In one pass an in O(1) space

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxMnt = 0
        i = 1
        n = len(arr)
        
        while i < n:
          # skip the equal element
            while i < n and arr[i-1] == arr[i]:
                i += 1
            # find the length of upHill
            up = 0
            while i < n and arr[i-1] < arr[i]:
                up += 1
                i += 1
            # find the length of downHill
            down = 0
            while i < n and arr[i-1] > arr[i]:
                down += 1
                i += 1
            # update the ans if there exist element both side
            if up > 0 and down > 0:
                maxMnt = max(maxMnt, up + down + 1)
        
        return maxMnt
