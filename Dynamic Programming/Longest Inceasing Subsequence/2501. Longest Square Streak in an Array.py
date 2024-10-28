# Logic: Just similar concept as LIS

# Method 1: Same as LIS
# Time: O(n^2), TLE
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[i] == nums[j] * nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans if ans >=2 else -1

# Method 2:
"""
Visualization: After seeing the pattern, maxiumum length can be equal to '5'.
Maximum nums[i] = 10**5.
How?
Say we start from smallest number i.e = 2 -> 2*2(4) -> 4*4(16) -> 16*16(256) -> 256*256(65536) -> >10**5.

So for each unique number check the longest subsequence we can form.
For this sort all the unique elements.
"""
# Time : O(n*logn) + O(5*n)-> maximum we need to check 5 times for each number
# Time : O(n*logn)

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = len(nums)
        numSet = set(nums)
        sorted_nums = sorted(list(numSet))
        visited = set()
        ans = 1
        for num in sorted_nums:
            if num in visited:
                continue
            visited.add(num)
            cur = num
            cnt = 1
            while cur * cur in numSet and cur*cur not in visited:
                cnt += 1
                cur *= cur
                visited.add(cur)
            ans = max(ans, cnt)
        return ans if ans >=2 else -1

# Method 3: Better one
# Time : O(n*logn)
"""
Logic: For each number check if square root is present.
i) If present then add '+1' to length of answer of its square root
ii) else put one in map for current number.
"""
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0
        nums.sort()
        
        for i in nums:
            root = int(math.sqrt(i))
            if root * root == i:
                dp[i] = dp.get(root, 0) + 1
            else:
                dp[i] = 1
            res = max(res, dp[i])
        
        return -1 if res < 2 else res

# Java: Method 3
"""
class Solution {
    public int longestSquareStreak(int[] nums) {
        HashMap<Integer, Integer> dp = new HashMap<>();
        int res = 0;
        Arrays.sort(nums);
        for(var i : nums){
            int root = (int)Math.sqrt(i);
            if(root * root == i)  
                dp.put(i, dp.getOrDefault(root, 0) + 1);
            else  
                dp.put(i, 1);
            res = Math.max(res, dp.get(i));
        }
        return res < 2 ? -1 : res;
    }
}

"""
        
