# Logic: if we replace every even number -> 0 and odd number -> 1 then 
# our q reduces to : Find no of subarray having sum = k i.e  "560. Subarray Sum Equals K".

# Note: if we were asked to find the no of subarray having count of even number is 'k' then we 
# will replace even number by '1' because here count of even number matters.

# Note vvi: Whenever you are asked to find answer based on odd & even
# try to convert them into '0/'1' depending upon question like whether to replace odd by '1' or even by '1'.
# And think of any logic.

# Time : O(n), 
# space : O(1)

# No need to change array , just add '1' when you see odd else '0' to curSum.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans,curr_sum= 0,0
        prefix_sum= {0:1}    # [sum: count_of_sum]
        for n in nums:
            curr_sum += 1 if n % 2 == 1 else 0
            diff = curr_sum - k  
            ans += prefix_sum.get(diff, 0)  
            prefix_sum[curr_sum] = 1+ prefix_sum.get(curr_sum, 0) 
        return ans
    

# Method 2:
# Time: O(n), space : O(1)

# Just exact same logic of q: "930. Binary Subarrays With Sum"
