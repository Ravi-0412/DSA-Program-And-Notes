# eaxctly same as 'longest substring with k distinct char'
# only change the condition i.e len(hashmap)<=k

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        freq= {}
        i, j= 0, 0
        ans= -1
        longest= ""  # will give any such string
        while j < len(s):
            freq[s[j]]= 1 + freq.get(s[j], 0)
            while len(freq) > k:
                freq[s[i]]-= 1
                if freq[s[i]]== 0:
                    del freq[s[i]]
                i+= 1
            ans= max(ans, j- i+ 1)  # for length we can update directly as here len(freq) <= k only.
            j+= 1
        return ans

# java
"""
import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        HashMap<Character, Integer> freq = new HashMap<>();
        int i = 0, j = 0, ans = -1;
        
        while (j < s.length()) {
            // Add the current character to the frequency map
            char currentChar = s.charAt(j);
            freq.put(currentChar, freq.getOrDefault(currentChar, 0) + 1);

            // If the number of unique characters exceeds k, shrink the window
            while (freq.size() > k) {
                char charAtI = s.charAt(i);
                freq.put(charAtI, freq.get(charAtI) - 1);
                if (freq.get(charAtI) == 0) {
                    freq.remove(charAtI);
                }
                i++;
            }
            ans = Math.max(ans, j - i + 1);
            j++;
        }
        
        return ans;
    }
}
"""
    
# Note : if asked this in circular array then , we can just add 'elements' from '0' to 'n-1' in original array at last 
# and apply the same logic.
# But in  this way our ans can exceed maximum ans i.e > len(arr).
# e.g: [2,2,2,2,2]  
# after appending: [2, 2, 2, 2, 2, 2, 2, 2, 2] so output= 9 but it ans should be = 5
# so for handling this return like: return ans if ans <= len(arr) else len(arr)

# Related Q:
# 1) 904. Fruit Into Baskets   => Asked me in Dezerv coding Round
