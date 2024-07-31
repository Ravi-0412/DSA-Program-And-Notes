# logic: if in any window if no of characters other than the most frequent char is <=k then that is valid case 
# and we can update our ans, we can replace these char with the most repeating char.

# My confusio:
# Note: No need to keep track of 'character' by which we are getting the maximum ans.
# If maxFreq becomes very big then also np because internal while loop won't run and
# whole window will be part of our ans which will be less than our ans till now.
# Also no need to update 'maxFreq' while sliding window from left.

# Time = Space = O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        FreqCount = {}  # will count the freq count in cur window
        maxFreq = 0   # will store the maximum frequency of any char in cur window.
        maxLength= 0  # will store the ans
        while j < len(s):
            FreqCount[s[j]]= 1+ FreqCount.get(s[j],0)
            maxFreq= max(maxFreq, FreqCount[s[j]])
            # We can only make 'k' char equal to char having maxFreq , so remove the extra char from starting of window.
            # If char having maxFreq is at start then, also it won;t affect the ans. Take exmaple and see.
            while (j -i + 1) - maxFreq > k:   
                FreqCount[s[i]]-= 1     
                i+= 1
            maxLength= max(maxLength, j - i + 1)
            j+= 1
        return maxLength


# Java 
""""
class Solution {
    public int characterReplacement(String s, int k) {
        int i = 0, j = 0;
        Map<Character, Integer> freqCount = new HashMap<>();
        int maxFreq = 0;   // will store the maximum frequency of any char in current window.
        int maxLength = 0;  // will store the answer

        while (j < s.length()) {
            freqCount.put(s.charAt(j), freqCount.getOrDefault(s.charAt(j), 0) + 1);
            maxFreq = Math.max(maxFreq, freqCount.get(s.charAt(j)));

            // We can only make 'k' characters equal to the character having maxFreq, so remove the extra characters from the start of the window.
            while ((j - i + 1) - maxFreq > k) {
                freqCount.put(s.charAt(i), freqCount.get(s.charAt(i)) - 1);
                i++;
            }

            maxLength = Math.max(maxLength, j - i + 1);
            j++;
        }

        return maxLength;
    }
}
"""
