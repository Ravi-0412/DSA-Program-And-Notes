# logic: similar to Q ."713. Subarray Product Less Than K"
# we need to keep track of minimum and max value in each window.
# Just traverse the array and keep on adding the current ele, and after adding find the valid subarray.

# What to do if invalid?
# We need to remove every ele from left side till we get valid window.
# We need to move the window from left side i. remove the leftmost ele till our window becomes valid.

# After getting the valid window, just add the length of valid window to our ans.

# Time: O(n^2)  , in reality will be less than this.
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i, j= 0, 0
        hashmap = collections.defaultdict(int)  # [ele : frequency]
        ans = 0
        while j < n:
            hashmap[nums[j]] += 1
            while max(hashmap.keys()) - min(hashmap.keys()) > 2:
                # try to remove the ele from start 
                hashmap[nums[i]] -= 1
                if hashmap[nums[i]] == 0:  # removing the ele from left side
                    del hashmap[nums[i]]
                i += 1
            ans += j - i + 1
            j += 1
        return ans
