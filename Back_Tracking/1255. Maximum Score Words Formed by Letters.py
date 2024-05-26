# Method 1:
# Logic : 1) Just find all subsets of words
# 2) check each subset whether valid or not.
# a) for this frequency of char used in subset should <= frequency of characters in letters.
# 3) if valid then return the score of each character in susbets

# time: O(2**w * w * l). w = len(words),l = len(each word)

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq_letters = Counter(letters)
        self.ans = 0
        n = len(words)

        def findScore(subset):
            freq = collections.defaultdict(int)
            sc = 0
            for w in subset:
                for c in w:
                    freq[c] += 1
                    if freq[c] > freq_letters[c]:
                        return 0
                    sc += score[ord(c) - ord('a')]
            return sc
                    
        def backtrack(i, subset):
            if i == n:
                self.ans = max(self.ans, findScore(subset))  # time: O(w * l)
                return
            backtrack(i +1, subset)
            backtrack(i + 1, subset + [words[i]])

        backtrack(0, [])
        return self.ans

# Method 2:
# better check the valid one before adding word[i].

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if not words or not letters or not score:
            return 0
        
        # Convert the letters list into a count of each letter
        count = [0] * 26
        for ch in letters:
            count[ord(ch) - ord('a')] += 1
        
        def backtrack(words, count, score, index):
            max_score = 0
            for i in range(index, len(words)):
                res = 0
                is_valid = True
                # Temporary decrease the count for the current word
                for ch in words[i]:
                    count[ord(ch) - ord('a')] -= 1
                    res += score[ord(ch) - ord('a')]
                    if count[ord(ch) - ord('a')] < 0:
                        is_valid = False
                if is_valid:
                    res += backtrack(words, count, score, i + 1)
                    max_score = max(res, max_score)
                # Restore the count after trying the current word
                for ch in words[i]:
                    count[ord(ch) - ord('a')] += 1
            return max_score
        
        return backtrack(words, count, score, 0)


# java
"""
// method 2:
class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        if (words == null || words.length == 0 || letters == null || letters.length == 0 || score == null || score.length == 0) return 0;
        int[] count = new int[score.length];
        for (char ch : letters) {
            count[ch - 'a']++;
        }
        int res = backtrack(words, count, score, 0);
        return res;
    }
    int backtrack(String[] words, int[] count, int[] score, int index) {
        int max = 0;
        for (int i = index; i < words.length; i++) {
            int res = 0;
            boolean isValid = true;
            for (char ch : words[i].toCharArray()) {
                count[ch - 'a']--;
                res += score[ch - 'a'];
                if (count[ch - 'a'] < 0) isValid = false;
            }
            if (isValid) {
                res += backtrack(words, count, score, i + 1);
                max = Math.max(res, max);
            }
            for (char ch : words[i].toCharArray()) {
                count[ch - 'a']++;
                res = 0;
            }
        }
        return max;
    }
}
"""