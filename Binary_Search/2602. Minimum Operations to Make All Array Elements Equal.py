# Logic: 
"""
1) If there are j numbers in nums that are smaller than query[i], 
you need to find query[i] * j - sum(j numbers smaller than query[i]) to find increments required in nums.
2) If there are k numbers in nums that are greater than query[i], 
you need to find sum(k numbers larger than query[i]) - query[i] * k to find decrements required in nums.
3) Sum of above two values is ans[i]
"""

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        # Compute prefix sums
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        results = []
        
        for q in queries:
            # Binary search to find the first element in nums[] that is >= q
            low, high = 0, n  # Here we are making high = n because in case q > max(nums) then
                              # low should point to 'n'.
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= q:
                    high = mid
                else:
                    low = mid + 1
            # Now, low is the number of elements in nums[] that are < q
            left = low   # Number of elements less than q
            right = n - low  # Number of elements greater than or equal to q
            
            # Calculate the total operations required
            left_operations = q * left - prefix_sum[left]
            right_operations = (prefix_sum[n] - prefix_sum[left]) - q * right
            
            total_operations = left_operations + right_operations
            results.append(total_operations)
        
        return results

# Other way , template 5

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        results = []
        
        for q in queries:
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= q:
                    high = mid - 1
                else:
                    low = mid + 1
            
            left = low   # Number of elements less than q
            right = n - low  # Number of elements greater than or equal to q
            
            left_operations = q * left - prefix_sum[left]
            right_operations = (prefix_sum[n] - prefix_sum[left]) - q * right
            
            total_operations = left_operations + right_operations
            results.append(total_operations)
        
        return results
