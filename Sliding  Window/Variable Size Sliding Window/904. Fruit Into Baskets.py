# Method 1:
# exactly same as : 340-longest-substring-with-at-most-k-distinct-characters1
# Time = O(n), space : O(1)

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # k is fixed at 2 because we only have two baskets
        k = 2
        freq = {}
        i = 0
        ans = 0
        
        for j in range(len(fruits)):
            # Add the current fruit to our 'baskets' (hash map)
            current_fruit = fruits[j]
            freq[current_fruit] = freq.get(current_fruit, 0) + 1
            
            # If we have more than 2 types of fruit, shrink the window from the left
            while len(freq) > k:
                left_fruit = fruits[i]
                freq[left_fruit] -= 1
                
                # If the count reaches zero, remove that fruit type from the baskets
                if freq[left_fruit] == 0:
                    del freq[left_fruit]
                
                i += 1
            
            # Update the maximum number of fruits collected so far
            # The length of the window is j - i + 1
            ans = max(ans, j - i + 1)
        return ans

# Other way
# Think a bit and understand with example : [1,5,5,4,5,1,2], ans = 4
# Tip: If you use this, always mention: "I'm using a non-shrinking sliding window to maintain the maximum size discovered so far in O(N) time."

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        i = 0
        
        for j in range(len(fruits)):
            freq[fruits[j]] = freq.get(fruits[j], 0) + 1
            
            # Optimization: Use 'if' instead of 'while'.
            # We let the window grow, but we never let it shrink below 
            # the maximum size we've already discovered.
            if len(freq) > 2:
                freq[fruits[i]] -= 1
                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]
                i += 1
        
        # The maximum window size is preserved until the end
        return j - i + 1




