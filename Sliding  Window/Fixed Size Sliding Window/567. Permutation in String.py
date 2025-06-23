# Method 1: 
# fully 100% same as "438. Find All Anagrams in a String" only
# here if you find any anargam then return true else return False instead of adding them into ans

# Time = space: O(n)

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count_s1 = Counter(s1)
        window = Counter(s2[:len1])

        if count_s1 == window:
            return True

        for i in range(len1, len2):
            start_char = s2[i - len1]
            end_char = s2[i]

            # Slide the window: remove start_char, add end_char
            window[end_char] += 1
            window[start_char] -= 1

            if window[start_char] == 0:
                del window[start_char]

            if window == count_s1:
                return True

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