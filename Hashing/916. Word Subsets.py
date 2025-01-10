# Subset means: arr1 should contain all ele of arr2 and quantity of all those ele in arr1 must be >= arr2.
# same with two string 

# Logic:
"""
Here we will check each string of words1 if that is universal or not.
For this we need to keep track of maximum frequency of all characters of string in words2.
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = collections.defaultdict(int)
        for word in words2:
            cur_freq = Counter(word)
            for c in word:
                max_freq[c] = max(max_freq[c], cur_freq[c])
                
        ans = []
        for word in words1:
            cur_freq = Counter(word)
            universalWord = True
            for k, v in max_freq.items():
                if cur_freq[k] < v:
                    universalWord = False
            if universalWord:
                ans.append(word)
        return ans

# java
"""
import java.util.*;

class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        // Create a frequency map to store the maximum frequency of each character in words2
        int[] maxFreq = new int[26];
        for (String word : words2) {
            int[] freq = countFrequency(word);
            for (int i = 0; i < 26; i++) {
                maxFreq[i] = Math.max(maxFreq[i], freq[i]);
            }
        }

        // Create a list to store the universal words
        List<String> result = new ArrayList<>();
        for (String word : words1) {
            int[] freq = countFrequency(word);
            boolean isUniversal = true;
            for (int i = 0; i < 26; i++) {
                if (freq[i] < maxFreq[i]) {
                    isUniversal = false;
                    break;
                }
            }
            if (isUniversal) {
                result.add(word);
            }
        }

        return result;
    }

    // Helper method to count the frequency of each character in a word
    private int[] countFrequency(String word) {
        int[] freq = new int[26];
        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }
        return freq;
    }
}
"""
