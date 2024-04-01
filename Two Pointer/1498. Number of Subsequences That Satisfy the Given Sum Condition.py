# We don't care the original elements order, We only care about minimum and maximum element in subsequence.
# So we can sort the original array, and the result won't change.

# Logic: For each element at starting index, find the next how much element it can include.
# For this we need to find the index of 'remaining_sum = target - nums[i]' on right side i.e from index 'i'.
# if no of element on right side*excluding nums[i] ) = n then, for each elemnet we have two choice either include that or not.

# Time: O(n^2), Tle
# Because of slicing of array after each index.

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mod = 10**9 + 7
        ans = 0
        for i in range(n):
            remaining_sum = target - nums[i]
            if remaining_sum < nums[i]:
                # on left side so skip
                continue
            r = bisect.bisect_right(nums[i : ], remaining_sum)  # Maximum 'r-1' element we can inlcude on right side from 'i'.
            
            no_ele = r - 1    # in 'r' already '-i' is done because of slicing 
            ans += 2 ** no_ele
        return ans % mod


# Method 2: Very better one
# Just two sum logic and above logic combination.

# Time = O(n*sqrt(n))

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mod = 10**9 + 7
        ans = 0
        i, j = 0, n -1
        while i <= j:
            if nums[i] + nums[j] <= target:
                # means this much ele we can include on right of 'i' and each will have 2 possibility.
                ans += 2 ** (j - i)
                i += 1
            else:
                j -= 1
        return ans % mod
        