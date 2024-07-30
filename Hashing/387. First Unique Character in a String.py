# Method 1:

# logic:
# Get the frequency of each character.
# Then find the first character that has a frequency of one.

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

# Method 2:
# store freq and first_index of each char in map.


"""

# Method 2:
# for each character store the count and 1st index in hashmap.

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

