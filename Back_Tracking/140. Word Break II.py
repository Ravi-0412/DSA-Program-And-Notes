# Method 1: 

"""
logic: just check which substring starting from start is present in 'dict, 
if it is present in dict then check for remaining string recursively and keep adding that to ans.

Time Complexity: O(2^n). Because there are 2^n combinations in worst case i.e when every char is present in the dictionary
in this case for every char we will have two options either to chose that char or not
space: O(n) recursive depth + O(n) for storing ans= O(n)

Cross Q / follow up 
NOte vvvi: "the same word in the dictionary may be reused multiple times in the segmentation.".
Due to this only we are able to check if cur substring of 's[i: j+ 1]' matches with any word in 'dict'.
If same word of dict is not allowed mutiple times then, we will have to take visited set for dict words(index will work)
to check whether the word at that index is already used or not.

Similar Questions:
1) "139. Word Break"
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dictSet = set(wordDict)
        ans = []

        def backtrack(i, sent):  # sent: sentence
            if i == n:
                ans.append(" ".join(sent))
                return
            for j in range(i, n):
                if s[i: j + 1] in dictSet:
                    backtrack(j + 1, sent + [s[i: j + 1]])
        backtrack(0, [])
        return ans

# Java Code
"""
import java.util.*;

class Solution {
    public void backtrack(int i, String s, Set<String> dictSet, List<String> sent, List<String> ans) {
        int n = s.length();
        if (i == n) {
            ans.add(String.join(" ", sent));
            return;
        }
        for (int j = i; j < n; j++) {
            String word = s.substring(i, j + 1);
            if (dictSet.contains(word)) {
                sent.add(word);
                backtrack(j + 1, s, dictSet, sent, ans);
                sent.remove(sent.size() - 1);
            }
        }
    }

    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dictSet = new HashSet<>(wordDict);
        List<String> ans = new ArrayList<>();
        List<String> sent = new ArrayList<>();
        backtrack(0, s, dictSet, sent, ans);
        return ans;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    void backtrack(int i, string &s, unordered_set<string> &dictSet, vector<string> &sent, vector<string> &ans) {
        int n = s.length();
        if (i == n) {
            string sentence = "";
            for (int j = 0; j < sent.size(); j++) {
                if (j > 0) sentence += " ";
                sentence += sent[j];
            }
            ans.push_back(sentence);
            return;
        }
        for (int j = i; j < n; j++) {
            string word = s.substr(i, j - i + 1);
            if (dictSet.find(word) != dictSet.end()) {
                sent.push_back(word);
                backtrack(j + 1, s, dictSet, sent, ans);
                sent.pop_back();
            }
        }
    }

    vector<string> wordBreak(string s, vector<string> &wordDict) {
        unordered_set<string> dictSet(wordDict.begin(), wordDict.end());
        vector<string> ans, sent;
        backtrack(0, s, dictSet, sent, ans);
        return ans;
    }
};
"""