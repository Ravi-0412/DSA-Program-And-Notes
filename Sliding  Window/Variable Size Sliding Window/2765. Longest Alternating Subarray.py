# Logic: Checking each subarray.

# Time: O(n^2)

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans= 0
        for i in range(n-1):
            for j in range(i + 1, n):
                if (j - i) % 2:
                    # ele at even places from starting subarray index 'i' , must have diff with pre one= '1'. (1,2,3...)
                    if nums[j] - nums[j -1] != 1:
                        break
                    ans = max(ans , j - i + 1)
                # ele at odd places from starting subarray index 'i' , must have diff with pre one= '-1'
                if (j - i) % 2 == 0:
                    if nums[j] - nums[j -1] != -1:
                        break
                    ans = max(ans , j - i + 1)
        return ans if ans != 0 else -1
    

# Shortcut of writing above
# How?
# Any alternating subarray must be of the form '2,3,2,3,2,3,........).
# So if we start our subarray from index 'i' then to form the alternating subarray 
# nums[j] must be equal to : 1) nums[i] + 1 if 'j' is at even place from 'i' (counting: 1,2,....)
# i.e one greater than 'nums[i]'
# 2) nums[j]= nums[i] + 0 = nums[i] only if 'j' is at odd place i.e same as 'nums[i]'.

# This will maintain the sequence of alternating subarray.

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans= 0
        for i in range(n-1):
            for j in range(i + 1, n):
                if nums[j] != (nums[i] + (j - i) % 2):
                    break
                ans = max(ans, j - i + 1)
        return ans if ans != 0 else -1


# Note vvi: In interview they will give higher constraint like n >= 10^5 or even >= 10^6.
# Then above logic will not work.
# so we have to optimise it.

# Time: O(n)

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1  # 'j' = 1 to check with pre ele.
              # 'i' : starting index of alternating subarray.
        ans= -1
        while j < n:
            if nums[j] == (nums[i] + (j - i) % 2):
                # If following the pattern
                ans = max(ans, j - i + 1)
            else:
                # we need to update 'i'.
                # we need to update 'i' either to 'j-1' or 'j' from where we can get alternating sequene.
                if nums[j] - nums[j - 1] == 1:
                    # Alternating sequence is starting from 'j-1'
                    i = j -1
                else:
                    i = j  # we have to look if there is new sequence starting from 'j'.
            j += 1
        return ans
    
# Note: Why we are not updating 'i' to 'i+1'?
# Ans: Because we only need to start from new sequence.
