# Note: If we try to find directly then we will miss some of the ans.
# e.g: Input: nums = [1,2,1,2,3], k = 2 ,Output: 7
# At index '2', no of distinct = 2 = len(frequency_hashmap) so [1,2,1] i.e from index 0 to 2 will get counted as ans.
# But how will we include [2, 1] ? 
# Same at index '3' , no of distinct = 2 = len(frequency_hashmap) so [1,2,1,2] i.e from index 0 to 3 will get counted as ans.
# But how will we include [2, 1,2] (index 1 to 3), [1, 2] (index 2 to 3) ...

# It will be very difficult to include these.

# My approch to add all but still was missing some answers.
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        count = {0: 1}
        ans = 0
        j = 0
        while j < n:
            freq[nums[j]] = 1 + freq.get(nums[j], 0)
            if len(freq) == k:
                ans += count[len(freq)] if len(freq) in count else 0
            count[len(freq)] = 1 + count.get(len(freq) , 0)
            ans += count[k - len(freq)] if (k - len(freq)) in count else 0
            # count[len(freq)] = 1 + count.get(len(freq) , 0)
            j += 1
        return ans

# Now coming to actual solution

# Combination of : 340-longest-substring-with-at-most-k-distinct-characters1 + 713. Subarray Product Less Than K

# Logic: 
# Count of SubArrays with K Distinct Elements = 
# Count of SubArrays with At Most K Distinct Elements - Count of SubArrays with At Most K-1 Distinct Elements

# Note : Whenever you are not able to find the ans directly then try to reduce it in other form i.e
# a) Think of finding its complement and get ans from that
# b) Think of finding ans for other thing and use that to get actual ans.

# Time = space = O(n)

# Note: For counting subarray
# Find the length of subarray after each element .
# Now agar pura subarray (valid one) me max 'k' distinct ele h then har ek subarray ka combination ans ka part hoga 
# And nya subarray jo hmko milega nums[i] add karne ke bad wo hoga = length of valid subarray

# Just similar to : 713. Subarray Product Less Than K

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def subarraysWithAtMostDistinct(nums, k):
            freq= {}
            i, j= 0, 0
            ans= -1
            longest= ""  # will give any such string
            while j < len(nums):
                freq[nums[j]] = 1 + freq.get(nums[j], 0)
                while len(freq) > k:
                    freq[nums[i]]-= 1
                    if freq[nums[i]]== 0:
                        del freq[nums[i]]
                    i+= 1
                ans += j - i + 1
                j+= 1
            return ans
        
        return subarraysWithAtMostDistinct(nums, k) - subarraysWithAtMostDistinct(nums, k -1)
    
# Other way:
# Number of subarrays having distinct elements equal to k =
# Total no. of subarrays - Number of subarrays having distinct elements smaller than k - Number of subarrays having distinct elements greater than k