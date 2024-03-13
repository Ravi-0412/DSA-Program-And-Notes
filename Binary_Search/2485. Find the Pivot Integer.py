

# Method 1:
# Logic: When we calculate prefix sum from both and right separately then 
# for any index we will get same value and that will be ans.

# Time: O()

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: 
            return 1
        prefix1 = [0]*n
        prefix1[0] = 1
        prefix2 = [0]*n
        prefix2[n -1] = n
        for i in range(1, n):
            prefix1[i] += prefix1[i -1] + (i + 1)
            prefix2[n - i - 1] += prefix2[n - i] + (n - i)
            
        for i in range(n):
            if prefix1[i] == prefix2[i]:
                return i + 1
        return -1
    

# # Method 2: 
# Can do using binary search by 3rd Template

# Logic: 1st find the prefix sum for 1 to n such that prefix[1] : Represents sum till n = 1 and so on.

# Then apply binary search taking : start = 1 and end = n

# Time: O(logn)
    

# Method 3: Mathematics
    
# Logic: Write sum of both left and right side then find 'x'.
# see: https://leetcode.com/problems/find-the-pivot-integer/solutions/2851991/sqrt-binary-search-dp/

# You will get x = sqrt(sum_till_n)

class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = n * (n + 1)//2
        x = int(sqrt(sum))
        return x if x *x == sum else -1