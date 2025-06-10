"""
Logic: We have to narrow the candidates after each time we call master.guess().
We have to find some strategy to 'get a similarity score between possible secret and a guess'.

Note : 1. If word has score x > 0, only those words that share exactly x characters with word can be the solution.
(Not word with lesser score nor with greater score).

Why?
e.g. suppose guess("xyz") = 1.

a) "abc" cannot be the solution because it shares 0 letters with "xyz". 
"xyz" has a score of 1 so "abc" must have at least 1 letter wrong to be the possible secret, so cannot be the solution.

b ) "zxy" cannot be the solution because it shares 0 letters (in the right place) with "xyz", so it must have at least one letter wrong.

c) "ayz" cannot be the solution because it shares 2 letters with "xyz". If "ayz" were the solution then "xyz" would have a score of 2.

d ) "abz" can be the solution because it shares 1 letter with "xyz".

Using above logic we can eliminate the possible secrets words.

But this on its own is not sufficient. We need to shrink the list faster for the big test cases.
For this we have to choose our guess based on some strategy to eliminate as max as possible to reach the secret fast.


How can be do this?

Intition: Use the most overlapping words
Why?
we want to find a word that overlaps most with other words so that we could eliminate all words that might have 0 matches with the guess word, 
this would help us to reach the secret asap.

1) choose the most overlapping word and check if it is secret word.
why to do by this ?
Ans: for most_overlapping words say 'w', guess function will return count of matched char  say 'x' then,
Next possible word must have matches == 'x' with most_overlapping words.
From this we can eliminate a lot of words

How to find the most overlapping words among all possible words?
Ans:  We need to take care of every position (here 0-5)and every position can have char from 'a-z'(0-25).
Means how many char matches at same position(index) among all the words.
for this we can make a matrix (position * char_index). char index for 'c' = ord(c) - ord("a") => this will bring in range of '0' to 25.
Now traverse each word and for every char just keep on adding '+1' for that cell (i, char_index).

At last again traverse each word and calculate the score same way we were doing '+1'.
The char having maximum score will be our most_overlapping character.

2) if most_overlaping is secret word then simply return 
3) Else find the possible secret words.(Explained above).

# time: O(w*l), w: no of words, l: length of each word
# time: O(26*6)
"""

class Solution(object):
    def findSecretWord(self, wordlist, master):
		
        def pair_matches(a, b):         # count the number of matching characters
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [[0 for _ in range(26)] for _ in range(6)]     # counts[i][j] is nb of words with char j at index i
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1  # keep adding '+1' at matrix cell (index *index_of_char)

            best_score = 0
            # calculate the score of each word
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord("a")]           # all words with same chars in same positions
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = wordlist.copy()        # all remaining candidates, initially all words
        while candidates:

            s = most_overlap_word()     # guess the word that overlaps with most others
            matches = master.guess(s)

            if matches == 6:
                # found the secret word so simply return
                return

            # Next possible word must have matches == 'matches' with most_overlapping words
            candidates = [w for w in candidates if pair_matches(s, w) == matches]   

# Java Code 
"""
import java.util.*;

interface Master {
    int guess(String word);
}

class Solution {
    private int pairMatches(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) count++;
        }
        return count;
    }

    private String mostOverlapWord(List<String> candidates) {
        int[][] counts = new int[6][26];  // counts[i][j] tracks frequency of char j at index i

        for (String word : candidates) {
            for (int i = 0; i < word.length(); i++) {
                counts[i][word.charAt(i) - 'a']++;
            }
        }

        int bestScore = 0;
        String bestWord = "";
        for (String word : candidates) {
            int score = 0;
            for (int i = 0; i < word.length(); i++) {
                score += counts[i][word.charAt(i) - 'a'];
            }
            if (score > bestScore) {
                bestScore = score;
                bestWord = word;
            }
        }

        return bestWord;
    }

    public void findSecretWord(String[] wordlist, Master master) {
        List<String> candidates = new ArrayList<>(Arrays.asList(wordlist));

        while (!candidates.isEmpty()) {
            String s = mostOverlapWord(candidates);
            int matches = master.guess(s);

            if (matches == 6) return;  // Found the secret word

            // Keep only words with 'matches' number of matching characters with the chosen word
            List<String> newCandidates = new ArrayList<>();
            for (String w : candidates) {
                if (pairMatches(s, w) == matches) {
                    newCandidates.add(w);
                }
            }
            candidates = newCandidates;
        }
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Master {
public:
    int guess(string word);
};

class Solution {
public:
    int pair_matches(const string& a, const string& b) {
        int count = 0;
        for (size_t i = 0; i < a.size(); i++) {
            if (a[i] == b[i]) count++;
        }
        return count;
    }

    string most_overlap_word(vector<string>& candidates) {
        vector<vector<int>> counts(6, vector<int>(26, 0));  // counts[i][j] tracks frequency of char j at index i

        for (const string& word : candidates) {
            for (size_t i = 0; i < word.size(); i++) {
                counts[i][word[i] - 'a']++;
            }
        }

        int best_score = 0;
        string best_word;
        for (const string& word : candidates) {
            int score = 0;
            for (size_t i = 0; i < word.size(); i++) {
                score += counts[i][word[i] - 'a'];
            }
            if (score > best_score) {
                best_score = score;
                best_word = word;
            }
        }

        return best_word;
    }

    void findSecretWord(vector<string>& wordlist, Master& master) {
        vector<string> candidates = wordlist;

        while (!candidates.empty()) {
            string s = most_overlap_word(candidates);
            int matches = master.guess(s);

            if (matches == 6) return;  // Found the secret word

            // Keep only words with 'matches' number of matching characters with the chosen word
            vector<string> new_candidates;
            for (const string& w : candidates) {
                if (pair_matches(s, w) == matches) {
                    new_candidates.push_back(w);
                }
            }
            candidates = move(new_candidates);
        }
    }
};
"""

