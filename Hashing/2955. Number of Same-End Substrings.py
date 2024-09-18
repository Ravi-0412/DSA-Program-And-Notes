# Logic: 
"""
For every substring, count how often each letter shows up. If a letter shows up 6 times, 
then there are 6+5+4+..+1 possible substrings that start and end in that letter.

Make it linear by keeping track of a subsum frequency of each letter, up to that index.
"""

# Time: O(26*n) = space

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Create a prefix sum array for each character
        prefix_sum_char = [[0 for _ in range(n + 1)] for _ in range(26)]
    
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            # Carry forward previous count for each character
            for j in range(26):
                prefix_sum_char[j][i + 1] = prefix_sum_char[j][i]
            # Increment count for the current character 
            prefix_sum_char[char_idx][i + 1] += 1  
        
        ans = []
        
        for l, r in queries:
            cnt = 0
            # For each character (from 'a' to 'z')
            for char_idx in range(26):
                # Frequency of the character in the substring s[l..r]
                freq = prefix_sum_char[char_idx][r + 1] - prefix_sum_char[char_idx][l]
                # Count substrings that start and end with this character
                cnt += (freq * (freq + 1)) // 2         
            ans.append(cnt)
        return ans

# java
"""
class Solution {
    public int[] sameEndSubstringCount(String s, int[][] queries) {
        int n = s.length();
        int[] result = new int[queries.length];
        
        // Create a prefix sum array for each character (26 for 'a' to 'z')
        int[][] prefixSumChar = new int[26][n + 1];

        // Fill the prefix sum array
        for (int i = 0; i < n; i++) {
            int charIdx = s.charAt(i) - 'a';
            // Carry forward previous count for each character
            for (int j = 0; j < 26; j++) {
                prefixSumChar[j][i + 1] = prefixSumChar[j][i];
            }
            // Increment count for the current character
            prefixSumChar[charIdx][i + 1]++;
        }

        // Process each query
        for (int q = 0; q < queries.length; q++) {
            int l = queries[q][0];
            int r = queries[q][1];
            int cnt = 0;
            
            // For each character ('a' to 'z')
            for (int charIdx = 0; charIdx < 26; charIdx++) {
                // Frequency of the character in the substring s[l..r]
                int freq = prefixSumChar[charIdx][r + 1] - prefixSumChar[charIdx][l];
                // Count substrings that start and end with this character
                cnt += (freq * (freq + 1)) / 2;
            }
            
            result[q] = cnt;
        }
        
        return result;
    }
}
"""
