# Logic: 
"""
Note: Just last and 1st element matter and sum between these two same element 
So we need to keep track of indices of each element.
And for sum between them we can use prefixSum concept.

Note: We store numbers and one of their index in a map.
We pick the "best" index using a Kadane algorithm

No need to store all the indices and compare with all. 

For checking the pair , just use same method as 'Two Sum' or best '2006. Count Number of Pairs With Absolute Difference K'.
For nums[i], we look for nums[i] + k (positive case) and nums[i] - k (negative case) in the map.
"""

# Time = space = O(n)

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = float('-inf')  # Equivalent to LLONG_MIN
        prefixSum = [0] * (n + 1)  # Prefix sum list
        indexMap = {}  # Dictionary to store indices of elements
        
        for i in range(n):
            # Calculate the prefix sum
            prefixSum[i + 1] = prefixSum[i] + nums[i]  
            
            # Positive case: Check if there's a previous subarray ending with 'nums[i] - k'
            if (nums[i] - k) in indexMap :
                ind = indexMap[nums[i] - k]
                res = max(res, prefixSum[i + 1] - prefixSum[ind])  # Update result for n - k
            # Negative case: Check if there's a previous subarray ending with nums[i] + k
            if (nums[i] + k) in indexMap :
                ind = indexMap[nums[i] + k]
                res = max(res, prefixSum[i + 1] - prefixSum[ind])  # Update result for n + k
            
            # Update the map if the current element is not present or the subarray sum is non-positive from last index 'indexMap[nums[i]]' to before 'i' then it's better to use 
            # replace index of 'nums[i]' with 'i'.
            # Otherwise no need to replace because some will increase only
            if nums[i] not in indexMap  or prefixSum[i] - prefixSum[indexMap[nums[i]]] <= 0:
                indexMap[nums[i]] = i
        
        # Return the result, if no valid subarray is found, return 0
        return res if res != float('-inf') else 0

# java
"""
import java.util.HashMap;

class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long res = Long.MIN_VALUE;
        long[] prefixSum = new long[n + 1];
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];  
            
            if (indexMap.containsKey(nums[i] - k)) {
                int ind = indexMap.get(nums[i] - k);
                res = Math.max(res, prefixSum[i + 1] - prefixSum[ind]);
            }
            
            if (indexMap.containsKey(nums[i] + k)) {
                int ind = indexMap.get(nums[i] + k);
                res = Math.max(res, prefixSum[i + 1] - prefixSum[ind]);
            }
            
            if (!indexMap.containsKey(nums[i]) || prefixSum[i] - prefixSum[indexMap.get(nums[i])] <= 0) {
                indexMap.put(nums[i], i);
            }
        }
        
        return res == Long.MIN_VALUE ? 0 : res;
    }
}
"""
