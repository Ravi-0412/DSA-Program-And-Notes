"""
Counting frequency will avoid duplication.
Time: O(k!), where k is the number of unique characters in tiles.
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(arr):
            total = 0
            for i in range(26):
                if arr[i] > 0:
                    total += 1  # all will be counted a sequence 
                    arr[i] -= 1
                    total += dfs(arr)
                    arr[i] += 1   # backtrack to explore other possibilities.`
            return total

        freq = [0] * 26
        for char in tiles:
            freq[ord(char) - ord('A')] += 1
        
        return dfs(freq)

# Java
"""
class Solution {
    public int numTilePossibilities(String tiles) {
        int[] arr = new int[26]; 
        for (char c : tiles.toCharArray()) {
            arr[c - 'A']++; 
        }
        return dfs(arr);
    }

    private int dfs(int[] arr) {
        int total = 0;
        for (int i = 0; i < 26; i++) {
            if (arr[i] > 0) {
                total++; // Count the current sequence
                arr[i]--; 
                total += dfs(arr); 
                arr[i]++; // Backtrack to explore other possibilities
            }
        }
        return total;
    }
}
"""

# To return all such sequence in a list
class Solution:
    def numTilePossibilities(self, tiles: str):
        def dfs(arr, path, result):
            # Iterate through all possible characters
            for i in range(26):
                if arr[i] > 0:
                    char = chr(i + ord('A'))  # Convert index back to character
                    new_path = path + char    # Form new sequence
                    
                    result.append(new_path)   # Add new sequence to the result
                    
                    arr[i] -= 1  # Decrease the count of the current character
                    dfs(arr, new_path, result)  # Recursively generate further sequences
                    arr[i] += 1  # Backtrack to explore other possibilities

        arr = [0] * 26  # Initialize the frequency array
        for char in tiles:
            arr[ord(char) - ord('A')] += 1  # Fill frequency array based on tiles

        result = []  # To store all the valid subsequences
        dfs(arr, "", result)  # Start DFS with an empty string

        return result  # Return the list of subsequences
