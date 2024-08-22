# Method 1: Brute force
# time: O(n*n*k), n = no of word, k = average length of each word

# Method 2: Accepted
# time: O(n*k*k)
# Link: https://leetcode.com/problems/palindrome-pairs/solutions/79209/accepted-python-solution-with-explanation/?envType=problem-list-v2&envId=ahiwan5d
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        # then adding 'back' to front of current 'word' will be a palindrome 
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):    
                    # checking j != n to avoid duplicate. Because when j == n then pref = word and this
                    # we have already checked in above case when j = 0 (in this suffix will be = word)
                    back = pref[::-1]
                    if back != word and back in words:
                        # then adding 'back' to last of current 'word' will be a palindrome
                        valid_pals.append([k, words[back]])
        return valid_pals
        
# shorter one
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref) and suf[::-1] != word and suf[::-1] in words:
                    # then adding 'back' to front of current 'word' will be a palindrome 
                    valid_pals.append([words[suf[::-1]],  k])
                if j != n and is_palindrome(suf) and pref[::-1] != word and pref[::-1] in words:    
                    # checking j != n to avoid duplicate. Because when j == n then pref = word and this
                    # we have already checked in above case when j = 0 (in this suffix will be = word).

                    # then adding 'back' to last of current 'word' will be a palindrome
                    valid_pals.append([k, words[pref[::-1]]])
        return valid_pals

# java
"""
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {

        HashMap<String, Integer> wordMap = new HashMap<>();
        List<List<Integer>> validPals = new ArrayList<>();

        // Storing words and their indices in the hashmap
        for (int i = 0; i < words.length; i++) {
            wordMap.put(words[i], i);
        }

        // Iterating through each word in the array
        for (int k = 0; k < words.length; k++) {
            String word = words[k];
            int n = word.length();

            // Splitting the word into a prefix and suffix at every possible position
            for (int j = 0; j <= n; j++) {
                String pref = word.substring(0, j);
                String suf = word.substring(j);

                // Check if the prefix is a palindrome
                if (isPalindrome(pref)) {
                    String back = new StringBuilder(suf).reverse().toString();
                    if (wordMap.containsKey(back) && wordMap.get(back) != k) {
                        // Adding 'back' to the front of 'word' will form a palindrome
                        List<Integer> pair = new ArrayList<>();
                        pair.add(wordMap.get(back));
                        pair.add(k);
                        validPals.add(pair);
                    }
                }

                // Check if the suffix is a palindrome
                if (j != n && isPalindrome(suf)) {
                    String back = new StringBuilder(pref).reverse().toString();
                    if (wordMap.containsKey(back) && wordMap.get(back) != k) {
                        // Adding 'back' to the end of 'word' will form a palindrome
                        List<Integer> pair = new ArrayList<>();
                        pair.add(k);
                        pair.add(wordMap.get(back));
                        validPals.add(pair);
                    }
                }
            }
        }
        return validPals;
    }

    // Helper method to check if a given string is a palindrome
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}

"""

# Later do by trie also
# will have same time complexity.