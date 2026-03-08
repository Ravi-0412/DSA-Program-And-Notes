# method 1: 

"""
Just extension of Question : 347. Top K Frequent Elements

Logic: since K is very small (K <= 100), the most efficient approach is to maintain a manually sorted "Top K" list and update it in-place.
When a new number comes in, or an existing number's frequency increases, you don't need to re-sort the entire history of N elements.
You only need to ensure that the one element you just changed is moved to its correct rank among the current leaders.

Time : O(n * K* logK) , O(k * logK) , for sorting everytime we see any element.
"""

class Solution:
    def kTop(self, arr, n, k):
        # Stores the frequency of each number seen so far
        frequency_map = {}
        # Stores the current top K elements in sorted order
        top_k_list = []
        # Final result storing top K at each step
        result = []

        for current_num in arr:
            # 1. Update the frequency of the current number
            frequency_map[current_num] = frequency_map.get(current_num, 0) + 1
            # 2. If the number is not in the top list, add it if there's room
            if current_num not in top_k_list:
                top_k_list.append(current_num)
            # 3. Re-sort the Top-K list based on the rules:
            # Rule A: Frequency (Descending)
            # Rule B: Value (Ascending) for equal frequency
            # Logic: Use -freq for descending and num for ascending in sort key
            top_k_list.sort(key=lambda x: (-frequency_map[x], x))
            # 4. Trim the list to only keep at most K elements
            if len(top_k_list) > k:
                top_k_list.pop()
            # Store a copy of the current state
            result.append(list(top_k_list))
        return result

# Method 2:
"""
Best one in , time : O(N * K)

Logic:
In the sorting version, we re-sort the entire list even though only one number's frequency changed.
We can use Insertion Sort logic (Bubbling). Since K is small (100), moving one element to its correct spot takes at most K steps.
"""
class Solution:
    def kTop(self, arr, n, k):
        frequency_map = {}
        top_k_list = []
        result = []

        for current_num in arr:
            # 1. Update frequency
            frequency_map[current_num] = frequency_map.get(current_num, 0) + 1
            
            # 2. Add to top_k_list if not already there
            if current_num not in top_k_list:
                top_k_list.append(current_num)
            
            # 3. Optimization: Manual Bubbling (Insertion Sort Logic)
            # Find where current_num is and move it left until it's in the right rank
            idx = top_k_list.index(current_num)
            
            while idx > 0:
                prev_num = top_k_list[idx - 1]
                curr_freq = frequency_map[current_num]
                prev_freq = frequency_map[prev_num]
                
                # Check if current_num should move ahead of prev_num:
                # Rule: Higher freq OR (Same freq and smaller value)
                if (curr_freq > prev_freq) or (curr_freq == prev_freq and current_num < prev_num):
                    # Swap
                    top_k_list[idx], top_k_list[idx-1] = top_k_list[idx-1], top_k_list[idx]
                    idx -= 1
                else:
                    break
            
            # 4. Enforce at most K elements
            if len(top_k_list) > k:
                top_k_list.pop()      
            # Store snapshot
            result.append(list(top_k_list))    
        return result






