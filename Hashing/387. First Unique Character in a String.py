# Method 1:

# logic:
# Get the frequency of each character.
# Then find the first character that has a frequency of one.
# time: O(n), space : O(26)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for i, char in enumerate(s):
            if freq[ord(char) - ord('a')] == 1:
                return i
        return -1


# java
"""
// Method 1:

public class Solution {
    public int firstUniqChar(String s) {
        int freq [] = new int[26];
        for(int i = 0; i < s.length(); i ++)
            freq [s.charAt(i) - 'a'] ++;
        for(int i = 0; i < s.length(); i ++)
            if(freq [s.charAt(i) - 'a'] == 1)
                return i;
        return -1;
    }
}
"""

# C++ Code 
"""
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> freq(26, 0);
        
        for (char c : s) {
            freq[c - 'a']++;
        }

        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i] - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
};
"""

# Method 2:
# for each character store the count and 1st index in hashmap.
# time: O(n), space : O(u) , u: No of distinct character in s

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}

        # Traverse the string to populate the map
        for i, c in enumerate(s):
            if c not in char_map:
                char_map[c] = [1, i]  # store count and first index
            else:
                char_map[c][0] += 1  # increment count

        # Initialize the result to be larger than any valid index
        result = len(s)

        # Iterate through the map to find the minimum index of characters that appear exactly once
        for count, index in char_map.values():
            if count == 1:
                result = min(result, index)

        # If no unique character is found, return -1
        return -1 if result == len(s) else result

# Java Code 
"""
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int firstUniqChar(String s) {
        Map<Character, int[]> charMap = new HashMap<>();

        // Traverse the string to populate the map
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!charMap.containsKey(c)) {
                charMap.put(c, new int[]{1, i}); // store count and first index
            } else {
                charMap.get(c)[0]++; // increment count
            }
        }

        // Initialize the result to be larger than any valid index
        int result = s.length();

        // Iterate through the map to find the minimum index of characters that appear exactly once
        for (Map.Entry<Character, int[]> entry : charMap.entrySet()) {
            if (entry.getValue()[0] == 1) {
                result = Math.min(result, entry.getValue()[1]);
            }
        }

        // If no unique character is found, return -1
        return result == s.length() ? -1 : result;
    }
}
"""

# C++ Code 
"""
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, pair<int, int>> freq_index; // {char : {freq, first_index}}

        for (int i = 0; i < s.size(); i++) {
            if (freq_index.count(s[i])) {
                freq_index[s[i]].first++; // Increment frequency
            } else {
                freq_index[s[i]] = {1, i}; // Store frequency and first index
            }
        }

        int min_index = s.size();
        for (const auto& [key, value] : freq_index) {
            if (value.first == 1) {
                min_index = min(min_index, value.second);
            }
        }

        return min_index == s.size() ? -1 : min_index;
    }
};
"""

