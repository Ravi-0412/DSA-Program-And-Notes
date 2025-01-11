# Logic:
"""
1) k <= len(s)
2) if some character has odd frequency then we there will be at least one palindrome and
this odd frequency character will be in middle surrounded by either same characters on left / right or by other characters.
Note: But no of this odd frequency character must be <=k 

3) For all other character having even freq we can rearrange in any way to form a palindrome
"""

# Time = O(n), space = O(26)

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        h = Counter(s)   # count freq of each character in 's'
        countOdd = 0
        for value in h.values():
            if value % 2:
                countOdd += 1
        return countOdd <= k

  # java
  """
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canConstruct(String s, int k) {
        // If k is greater than the length of the string, it's not possible
        if (k > s.length()) {
            return false;
        }
        
        // Count the frequency of each character in the string
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        // Count the number of characters with odd frequency
        int countOdd = 0;
        for (int count : charCount.values()) {
            if (count % 2 != 0) {
                countOdd++;
            }
        }
        
        // If there are more odd frequencies than k, it's not possible
        return countOdd <= k;
    }
}
  """
