# to get the maximum sum in 'k' operation we will pick each time max ele only.
# for this 1st find the max ele and then each operation we have to incr this.

# Time = Max(n, k)

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_ele= max(nums)
        sum= 0
        for i in range(k):
            sum+= max_ele
            max_ele+= 1  # incr each time max_ele by 1
        return sum

# Other way
# Logic: Find maximum element + formula 
class Solution:
    def maximizeSum(self, n: List[int], k: int) -> int:
        return  k * max(n) + k * (k - 1) // 2;
