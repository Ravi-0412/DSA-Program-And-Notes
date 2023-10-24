# Logic: nums[j] is the last number in the required subsequence. 
# Since we need to maximize the sum of the numbers in the subsequence,
# the previous number in the subsequence could be max(nums[j-1], nums[j-2], ..., nums[j-i], ..., nums[j-k]) where j-i >= 0.
# However, if all nums[j-1], nums[j-2], ..., nums[j-i], ..., nums[j-k] are negative, there would be no previous number,
#  as it would lower the required sum.

#  F(j) denote the maximum sum of the subsequence with nums[j] as the last number.
# F(j) = nums[j] + max(0, F(j-1), F(j-2), ..., F(j-i), ... F(j-k)) where j-i >= 0.
# Note that if all of the valid F(j-1), F(j-2), ..., F(j-i), ... F(j-k) are negative, 
# we will not choose any of these values because choosing one of them would 
# lower the value of the required sum: hence we have a 0 in the max term.

# Recurrence relation: 
# F(n) = F(n-1) + F(n-2) + ... + F(n-k)
# .
# .
# .
# F(0) = 1

# If you draw a recursion tree, it will be a k-ary tree with depth n, where n is the length of nums. 
# 'The time complexity is the number of nodes in this tree, O(k^n). The space complexity is the depth of this tree (recursion stack), O(n)
# without memoisation.

# With memoisation:
# Time : O(n*k), space = O(n)
# Reason: F(j) is processed at most once, where j is in the range [0, n-1], inclusive. 
# To determine each F(j), we recursively call F(j-1), F(j-2), ..., F(j-i), ... F(j-k).
# Hence, for each F(j), we do k amount of work. Think of it as using a for loop with k iterations. 
# Since there are n such calls to F(j) as described previously, we do n*k amount of work overall. Hence, the time complexity is O(nk).

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        def solve(j):
            if j < 0:
                return 0
            max_val = 0
            for i in range(1, k + 1):
                max_val = max(max_val , solve(j - i))
            return nums[j] + max_val  # return with nums[j]

        ans = float('-inf')
        for i in range(len(nums)):
            ans = max(ans, solve(i))
        return ans

# Writing above code like this will give wrong ans
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        def solve(j):
            if j < 0:
                return 0
            max_val = nums[j]
            for i in range(1, k + 1):
                max_val = max(max_val , solve(j - i))
            return max_val

        ans = float('-inf')
        for i in range(len(nums)):
            ans = max(ans, solve(i))
        return ans


# Mine logic:
# But it's not working
# Reason: We are skipping and then considering some ele 
# So next index should be in range 'k' is not getting maintained.
# i.e j -i <= k

# So this will give max_possible_sum of array.

# Note: Keep in mind that everytime 'take' and 'notTake' doesn't work.

# Note: Here we need to call function separately for each index for correct ans.
# Will ask someone if we can do like this i.e not calling function for each index separately.

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        def solve(i):
            if i >= len(nums):
                return float('-inf')
            notTake = solve(i + 1)
            take = nums[i]
            for j in range(1, k + 1):
                take = max(take , nums[i] + solve(i + j))
            return max(take, notTake)

        return solve(0)


# Tabulation
# dp[j] represents the maximum sum of the subsequence with nums[j] as the last element. 
# dp[j] = nums[j] + max(0, dp[j-1], dp[j-2], ..., dp[j-i], ..., dp[j-k]), where j-i >= 0

# Same we 'Longest Increasing subsequence'.

# Time : O(n*k), space = O(n)

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for j in range(1, n):
            back = max(j-k, 0)  # we can take any index from 'j-k' to 'j-1' for dp[j]
            for i in range(back , j):
                dp[j]= max(dp[j] , dp[i])
            dp[j] += nums[j]
        return max(dp)


# If you will write like this, will give wrong ans.
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [nums[i] for i in range(n)]
        for j in range(1, n):
            for i in reversed(range(max(0, j - k), j)):
                dp[j]= max(dp[j] , dp[i])
        return max(dp)


# Method 3:
# Optimising using logic of "239. Sliding Window Maximum".

# Time : O(n)
# Space : O(K), Because at most O(K) elements in the deque.

from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = deque([0])  # Mono decreasing queue. will store the possible indexe
            # we need to take maximum from pre 'j-k' ele so decreasing queue.

        for j in range(1, n):
            # remove all indexes which is out of window for cur index 'j'
            # i.e for 'j' , we need to consider from index 'j-k' to 'j-1'.
            # so remove all index < 'j-k' from queue.
            # for this we need to remove from start of 'q'.
            while q and q[0] < j - k:
                q.popleft()
            # Since 'q' is decreasing one so best possible condidate
            # for 'j' will be 1st index in 'q'
            dp[j] = nums[j] + max(0, dp[q[0]])
            # Now pop all those indexes which has 'dp' value less than 'j'.
            # Because why to consider index before 'j' for next upcoming index if dp[j]' has greater value.
            # for this we need to remove from last
            while q and dp[q[-1]] < dp[j]:
                q.pop()
            # Now append 'j' to 'queue'.
            q.append(j)
        return max(dp)
