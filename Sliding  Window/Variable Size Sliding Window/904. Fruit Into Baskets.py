# Method 1:
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

