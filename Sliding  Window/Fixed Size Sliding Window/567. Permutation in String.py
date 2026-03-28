# Method 1: 
# fully 100% same as "438. Find All Anagrams in a String" only
# here if you find any anargam then return true else return False instead of adding them into ans

# Time = space: O(n)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is longer than s2, no permutation can exist
        if len(s1) > len(s2):
            return False
            
        # Step 1: Create frequency map for s1 (the target)
        char_map = {}
        for char in s1:
            char_map[char] = char_map.get(char, 0) + 1
            
        # 'count' tracks unique characters in s1 that need to be matched
        count = len(char_map)
        
        # Pointers for the sliding window
        left, right = 0, 0
        window_size = len(s1)
        
        # Step 2: Iterate through s2
        while right < len(s2):
            char_right = s2[right]
            
            # If the character is part of our target permutation
            if char_right in char_map:
                char_map[char_right] -= 1
                # If we've satisfied the required frequency for this specific char
                if char_map[char_right] == 0:
                    count -= 1
            
            # Step 3: Check if the window has reached the required size
            if right - left + 1 == window_size:
                # If all unique character frequencies match (count is 0)
                if count == 0:
                    return True
                
                # Step 4: Shrink the window from the left to slide it forward
                char_left = s2[left]
                if char_left in char_map:
                    # If this character was previously satisfied, increment count
                    if char_map[char_left] == 0:
                        count += 1
                    char_map[char_left] += 1
                
                left += 1
                
            right += 1
            
        return False
        

# Java Code 
"""
import java.util.*;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2)
            return false;

        Map<Character, Integer> countS1 = new HashMap<>();
        for (char c : s1.toCharArray())
            countS1.put(c, countS1.getOrDefault(c, 0) + 1);

        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < len1; i++)
            window.put(s2.charAt(i), window.getOrDefault(s2.charAt(i), 0) + 1);

        if (window.equals(countS1))
            return true;

        for (int i = len1; i < len2; i++) {
            char startChar = s2.charAt(i - len1);
            char endChar = s2.charAt(i);

            // Slide the window: remove startChar, add endChar
            window.put(endChar, window.getOrDefault(endChar, 0) + 1);
            window.put(startChar, window.get(startChar) - 1);

            if (window.get(startChar) == 0)
                window.remove(startChar);

            if (window.equals(countS1))
                return true;
        }

        return false;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int len1 = s1.size(), len2 = s2.size();
        if (len1 > len2) return false;

        unordered_map<char, int> countS1;
        for (char c : s1) countS1[c]++;

        unordered_map<char, int> window;
        for (int i = 0; i < len1; ++i)
            window[s2[i]]++;

        if (window == countS1) return true;

        for (int i = len1; i < len2; ++i) {
            char startChar = s2[i - len1];
            char endChar = s2[i];

            // Slide the window: remove startChar, add endChar
            window[endChar]++;
            window[startChar]--;

            if (window[startChar] == 0)
                window.erase(startChar);

            if (window == countS1)
                return true;
        }

        return false;
    }
};
"""
