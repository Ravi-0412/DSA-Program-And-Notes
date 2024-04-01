# Logic: Just solve the reverse question by sliding window i.e 
# Solve for number of subarrays where the maximum appears less than k times 
# and return total number of possible subarrays minus the answer you got!

# After inserting each ele find the valid subarray 'number of subarrays where the maximum appears less than k times ' .
# If freq in that valid subarray is <= k then all possible new subarray we can make after adding the current ele will get added in ans.
# Just like : 713. Subarray Product Less Than K

# Time = O(n), space = O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        ans = 0
        maxEle = max(nums)
        i, j = 0, 0
        while j < n :
            if nums[j] == maxEle:
                cnt += 1
            while i <= j and cnt >= k:   # i<= j , for k == 1
                if nums[i] == maxEle:
                    cnt -= 1
                i += 1
            ans += j - i + 1
            j += 1

        total_possible_subarray = (n *(n + 1)) //2
        return total_possible_subarray - ans


# Method 2: Good one
# After each ele at index 'j' , if cnt >= k then we can include all ele from 'j' to 'n-1' and all will be valid ans only 
# for all valid 'i' until we find 'i' such that from 'i' to curr 'j' subarray is invalid.
    
# So keep on adding 'n- j' in ans after each ele until you find any invalid subarray.
    
    # Time = O(n), space = O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        ans = 0
        maxEle = max(nums)
        i, j = 0, 0
        while j < n :
            if nums[j] == maxEle:
                cnt += 1
            while cnt >= k:
                if nums[i] == maxEle:
                    cnt -= 1
                i += 1
                ans += n - j   
            j += 1
        return ans