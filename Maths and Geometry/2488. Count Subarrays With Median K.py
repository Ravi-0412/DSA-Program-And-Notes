# Method 1:
"""
1. 'k' must be present in the array because numbers ranges are from '1 to N'.
2. Every valid subarray must contain 'K'

Logic: 
To find the median k in a subarray of distinct integers:
1. Identify the Pivot: Find the index of k. Every valid subarray must include this index.
2. Relative Counting: Instead of sorting, we only care about the count of elements Greater (G) and Smaller (S) than k.
3. Odd-Length Subarrays: k is the median if there are equal numbers on both sides.
Logic: G=S (or G−S=0).

4. Even-Length Subarrays: Since the median is the "left-middle" element, k must be one of the two middle values.
Logic: G=S+1 (one more element on the right/greater side to keep k in the left-middle position).

Time : O(N^2), Check every possible start and end point, update G and S, and see if the conditions above are met while k is inside the window.
"""
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Edge case: If k isn't in the list, no subarray can have it as a median.
        if k not in nums:
            return 0
        # Every valid subarray MUST include the position of k.
        median_pos = nums.index(k)
        valid_subarrays = 0
        # Try every possible starting point 'i' for a subarray
        for start in range(n):
            smaller_count = 0
            greater_count = 0
            # Expand the subarray from 'start' to every possible 'end' point 'j'
            for end in range(start, n):
                # We only care about relative size: 
                # Is the number bigger or smaller than our target k?
                if nums[end] > k:
                    greater_count += 1
                elif nums[end] < k:
                    smaller_count += 1
                  
                # RULE 1: The subarray must contain the actual element 'k'.
                # We only check the median property if the current window [start...end] covers median_pos.
                if start <= median_pos <= end:
                    length = end - start + 1

                    # RULE 2: Odd length subarrays.
                    # k is the median if there are an equal number of elements on its left and right.
                    # Mathematically: greater_count == smaller_count
                    if length % 2 == 1 and greater_count == smaller_count:
                        valid_subarrays += 1

                    # RULE 3: Even length subarrays.
                    # Per problem description: if even, median is the "left-middle" element.
                    # For k to be the left-middle, there must be exactly one more 'greater' 
                    # element than 'smaller' elements (e.g., [1, k, 4, 5] -> S:1, G:2).
                    elif length % 2 == 0 and (greater_count - smaller_count) == 1:
                        valid_subarrays += 1

        return valid_subarrays

# method 2:
"""
Most optimised one
Link: https://leetcode.com/problems/count-subarrays-with-median-k/solutions/2852402/python3-hashmap-counting-explained-on-by-68tc/ 

1. We can check the elements before k and after k, and count the number of elements larger/smaller than k.
2. let's use l1 and s1 denoting the number of elements larger and smaller than k, Before k.
and l2, s2 denoting the number of elements larger and smaller than k, After k.
=> The above equation becomes:
l1 + l2 == s1 + s2 => l1 - s1 == s2 - l2
l1 + l2 == s1 + s2 + 1 => l1 - s1 == s2 - l2 + 1
3. Now we can use a hash map to count the frequency of l1 - s1 for the subarray before k (and contains k).
4. Then, check if s2 - l2 and s2 - l2 + 1 in the hash map for the subarray after k (and contains k) to compute the result.

from code perspective: 
1. Pivot Identity: We locate k. Any valid subarray must include this index.
2. Left Pass: We calculate the balance of elements before k. A balance of +1 means there is one more element > k than < k. We store these frequencies.
3. Right Pass: We do the same for elements after $k$.
4. The "Meeting" Condition:
  To be a median in an odd length array: Left_Balance + Right_Balance == 0.
  To be a median in an even length array: Left_Balance + Right_Balance == 1.

Time : o(N), space = O(N)
"""

from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # Step 1: Locate the position of k. 
        # Since integers are distinct, this index is unique.
        pivot_index = nums.index(k)
        
        # 'counts_before' will store how many times a specific 
        # (Larger - Smaller) balance occurs to the left of k.
        counts_before = defaultdict(int)
        
        total_valid_subarrays = 0
        larger_count = 0
        smaller_count = 0
        
        # Step 2: Traverse Left from the pivot (exclusive)
        for i in range(pivot_index - 1, -1, -1):
            if nums[i] > k:
                larger_count += 1
            else:
                smaller_count += 1
            
            current_balance = larger_count - smaller_count
            counts_before[current_balance] += 1
            
            # If the current left-side subarray [i...pivot_index] is already 
            # valid (median is k), increment the result.
            if current_balance == 0 or current_balance == 1:
                total_valid_subarrays += 1

        # Reset counts for the right-side traversal
        larger_count = 0
        smaller_count = 0
        
        # Step 3: Traverse Right from the pivot (exclusive)
        for i in range(pivot_index + 1, len(nums)):
            if nums[i] > k:
                larger_count += 1
            else:
                smaller_count += 1
                
            current_balance = larger_count - smaller_count
            
            # We need (Left_Balance + Right_Balance) to be 0 or 1.
            # 1. Target 0: Left_Balance = -Right_Balance (s2 - l2)
            # 2. Target 1: Left_Balance = 1 - Right_Balance (s2 - l2 + 1)
            total_valid_subarrays += counts_before[-current_balance]
            total_valid_subarrays += counts_before[1 - current_balance]
            
            # If the current right-side subarray [pivot_index...i] is 
            # already valid, increment the result.
            if current_balance == 0 or current_balance == 1:
                total_valid_subarrays += 1
                
        # Return total plus 1 (to account for the single-element subarray [k])
        return total_valid_subarrays + 1

# method 3:
"""
Just little concise way to write Method 2
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Step 1: Find the position of k (the pivot)
        # The problem guarantees distinct integers, so index is unique.
        pivot_idx = nums.index(k)
        n = len(nums)
        
        # Step 2: Traverse Left from the pivot
        # count_map stores: {balance: number_of_occurrences}
        count_map = Counter()
        balance = 0
        count_map[0] = 1 # Base case: the subarray [k] itself has balance 0
        
        for i in range(pivot_idx - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1
            count_map[balance] += 1
            
        # Step 3: Traverse Right from the pivot and match with Left
        total_valid = 0
        balance = 0 # Reset balance for the right side
        
        for i in range(pivot_idx, n):     # if you start from pivot_ind + 1 then you will miss case where nums[i] = k
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            
            # Condition 1: Odd length (G - S = 0)
            # We need: balance + left_balance == 0  => left_balance = -balance
            total_valid += count_map[-balance]
            
            # Condition 2: Even length (G - S = 1)
            # We need: balance + left_balance == 1  => left_balance = 1 - balance
            total_valid += count_map[1 - balance]
            
        return total_valid

# Follow ups:
"""
Q) What if duplicates are allowed and numbers are random?
Solve by prefixSum logic and Segment Tree.

Question link: https://www.geeksforgeeks.org/problems/median-of-the-subarrays--170647/1
"""
