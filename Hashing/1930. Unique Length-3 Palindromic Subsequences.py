# Logic
"""
We track the first and last occurence of each character.

Then, for each character, we count unique characters between its first and last occurence. 
That is the number of palindromes with that character in the first and last positions.

Example: abcbba, we have two unique chars between first and last a (c and b), 
and two - between first and last b (b and c). No characters in between c so it forms no palindromes.

time: O(n), space: O(26)
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [-1] * 26
        res = 0
        
        # Record the first and last occurrences of each character
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            first[index] = min(first[index], i)
            last[index] = i
        
        # Count distinct characters between first and last occurrence of each character
        for i in range(26):
            if first[i] < last[i]:
                unique_chars = set(s[first[i] + 1:last[i]])
                res += len(unique_chars)
        
        return res

# Java
"""
class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] first = new int[26], last = new int[26];
        Arrays.fill(first, Integer.MAX_VALUE);
        Arrays.fill(last, -1);
        int result = 0;

        // Record first and last occurrences of each character
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            first[idx] = Math.min(first[idx], i);
            last[idx] = i;
        }

        // Count unique characters between first and last indices
        for (int i = 0; i < 26; i++) {
            if (first[i] < last[i]) {
                boolean[] seen = new boolean[26];
                for (int j = first[i] + 1; j < last[i]; j++) {
                    seen[s.charAt(j) - 'a'] = true;
                }
                for (boolean b : seen) if (b) result++;
            }
        }

        return result;
    }
}
"""

# C++ Code 
"""
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<int> first(26, INT_MAX), last(26, -1);
        int res = 0;

        // Record the first and last occurrences of each character
        for (int i = 0; i < s.size(); i++) {
            int index = s[i] - 'a';
            first[index] = min(first[index], i);
            last[index] = i;
        }

        // Count distinct characters between first and last occurrence of each character
        for (int i = 0; i < 26; i++) {
            if (first[i] < last[i]) {
                unordered_set<char> unique_chars(s.begin() + first[i] + 1, s.begin() + last[i]);
                res += unique_chars.size();
            }
        }
        return res;
    }
};
"""
