# method 1: brute force
# Logic: Just convert each string into set and compare set for each pair.

# Time: O(n^2), space = O(n^2)

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getCharSet(word):
            return set(word)
        
        n = len(words)
        char_sets = [getCharSet(word) for word in words]
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                set_i = char_sets[i]
                set_j = char_sets[j]
                no_common_characters = True
                for char in set_i:
                    if char in set_j:
                        no_common_characters = False
                        break    
                if no_common_characters:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        return max_product

# using inbuilt set function in python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getCharSet(word):
            return set(word)
        
        n = len(words)
        char_sets = [getCharSet(word) for word in words]
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if char_sets[i].isdisjoint(char_sets[j]):
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        return max_product

# java
"""
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public int maxProduct(List<String> words) {
        Set<Character> getCharSet(String word) {
            Set<Character> charSet = new HashSet<>();
            for (char c : word.toCharArray()) {
                charSet.add(c);
            }
            return charSet;
        }
        
        int n = words.size();
        Set<Character>[] charSets = new HashSet[n];
        
        for (int i = 0; i < n; i++) {
            charSets[i] = getCharSet(words.get(i));
        }
        
        int maxProduct = 0;
        
        // Iterate through each pair of words
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isDisjoint(charSets[i], charSets[j])) {
                    int product = words.get(i).length() * words.get(j).length();
                    maxProduct = Math.max(maxProduct, product);
                }
            }
        }
        
        return maxProduct;
    }

    private boolean isDisjoint(Set<Character> set1, Set<Character> set2) {
        for (Character c : set1) {
            if (set2.contains(c)) {
                return false;
            }
        }
        return true;
    }
}

"""

# Method 2: Using Bit Masking
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getBitmask(word: str) -> int:
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))
            return bitmask
        
        n = len(words)
        bitmasks = [getBitmask(word) for word in words]
        max_product = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:  # No common letters
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        
        return max_product

