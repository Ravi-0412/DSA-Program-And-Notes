# for max ans, longest ke liye jitna se jitna char repeat karne chahiye with 

# Note: To check the number of unique char at any point of time we will use hashmap.
# len(ahshmap): will tell no of unique char at any point of time.

# time: O(n)= space 

# shorter way and concise way.
# Note: Try to solve every variable sliding window problem like this only.
# After seeing every char check for valid substring and update ans.

class Solution:
    def longestKSubstr(self, s, k):
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
            if len(freq)== k and j - i + 1 > ans:
                longest= s[i: j +1]
                ans= max(ans, j- i+ 1)
            j+= 1
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int longestKSubstr(String s, int k) {
        Map<Character, Integer> freq = new HashMap<>();
        int i = 0, j = 0;
        int ans = -1;
        String longest = "";  // will give any such string

        while (j < s.length()) {
            freq.put(s.charAt(j), freq.getOrDefault(s.charAt(j), 0) + 1);
            while (freq.size() > k) {
                char ch = s.charAt(i);
                freq.put(ch, freq.get(ch) - 1);
                if (freq.get(ch) == 0) {
                    freq.remove(ch);
                }
                i++;
            }
            if (freq.size() == k && (j - i + 1) > ans) {
                longest = s.substring(i, j + 1);
                ans = Math.max(ans, j - i + 1);
            }
            j++;
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int longestKSubstr(string s, int k) {
        unordered_map<char, int> freq;
        int i = 0, j = 0;
        int ans = -1;
        string longest = "";  // will give any such string

        while (j < s.size()) {
            freq[s[j]]++;
            while (freq.size() > k) {
                freq[s[i]]--;
                if (freq[s[i]] == 0) {
                    freq.erase(s[i]);
                }
                i++;
            }
            if (freq.size() == k && (j - i + 1) > ans) {
                longest = s.substr(i, j - i + 1);
                ans = max(ans, j - i + 1);
            }
            j++;
        }

        return ans;
    }
};
"""


