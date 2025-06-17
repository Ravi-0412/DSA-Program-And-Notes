# Method 1: 

# Logic: we can convert this problem into: " 198. House Robber"
# for this just take only distinct ele and sort.

# then we only need to check with next index 'i+1' if that has value = nums[i] + 1 or not.
# if has then skip or take that.

# Note: We can take all the occurence of any ele if we take that.
# for this store the frequency also if you take then points = freq[nums[i]] * nums[i].

"""
As per the problem statement, we'll try to understand seeing an example.
for example, you took 3 then you will get 3*(how many times 3 occurs) but you cannot pick 2 and 4 anymore.
so the logic is first we count the occurance of each element in a freq array.
then take only distinct/unique elements only cause we know if we select 3 and it appears 4 times, we know choosing 3 gives us 3 * 4 = 12 points, so no harm to take the unique elemnts.
and then sort it cause sorting makes  it easier to calculate the max points as it is in increasing order and we are checking if the next element is exactly +1 than the current element or not.
now, it is similar to house robber problem.
take and not_take approach-
take the ith element(lets say nums[i]) and skip the next one (lets say nums[i+1]) if it is exactly nums[i]+1
or we can skip the ith element and move to the next one simply.
finally, choose the max points among both.
"""

# Time:  O(n*logn) 

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)

        def solve(i):
            if i >= n:
                return 0 
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i] 
            take += solve(i + 1) if i + 1 < n  and nums[i + 1] != nums[i] + 1 else solve(i + 2)
            return max(take, notTake)

        return solve(0)

# Method 2: 
#Memoisation
#time: O(n) (logn for soritng), space : O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [-1] * n  # memoization array

        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]

            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i]
            if i + 1 < n and nums[i + 1] != nums[i] + 1:
                take += solve(i + 1)
            else:
                take += solve(i + 2)
            dp[i] = max(take, notTake)
            return dp[i]

        return solve(0)


# Method 3: 
# Tabulation
#time: O(n) (logn for soritng), space : O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter

        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp = [0] * (n + 2)  # Extra space for bounds

        for i in range(n - 1, -1, -1):
            notTake = dp[i + 1]
            take = freq[nums[i]] * nums[i]
            if i + 1 < n and nums[i + 1] != nums[i] + 1:
                take += dp[i + 1]
            else:
                take += dp[i + 2]
            dp[i] = max(take, notTake)

        return dp[0]
