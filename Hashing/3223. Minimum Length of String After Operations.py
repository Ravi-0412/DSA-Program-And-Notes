# logic:
"""
suppose any char has freq 'v' then all will get cancelled except either one or two character.
If 'v' is even then : 2 char will be remaining else only '1' char
"""

# time = space = O(n)

from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for val in freq.values():
            ans += 2 if val % 2 == 0 else 1
        return ans

  # Java
  """
  import java.util.HashMap;

class Solution {
    public int minimumLength(String s) {
        HashMap<Character, Integer> freq = new HashMap<>();
        int ans = 0;
        
        // Count frequency of each character in the string
        for (char ch : s.toCharArray()) {
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }
        
        // Calculate the result based on frequencies
        for (int val : freq.values()) {
            ans += (val % 2 == 0) ? 2 : 1;
        }
        
        return ans;
    }
}
  """
