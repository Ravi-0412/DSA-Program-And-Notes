# Logic: While traversing each word we have to match it with pre seen 'word'
# having same freq count of each ele (i.e anargam).

# Method 1:
# just used the meaning of anargam like when sorted they should be same.
# time: O(m*n*logn)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)    # sorted : return list so converting into tuple because list can't be key.
        return hashmap.values()


# Method 2: 

# same method as we find all anargams.
# time: O(m*n*26). m: #words, n: # char in each word.
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)
        for s in strs:
            count= [0]*26   # to store the count of each char for each string.   a.....z
            for c in s:
                count[ord(c)- ord("a")]+= 1
            # append all string with these number of char count as key.
            # changing into tuple because list can't be key.
            hashmap[tuple(count)].append(s)    
        return hashmap.values()

# Java Code
"""
import java.util.*;

// Method 1: Using sorted strings as keys
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashmap = new HashMap<>();

        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray); // Sorting to check anagram validity
            String sorted_s = new String(charArray);
            
            hashmap.computeIfAbsent(sorted_s, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(hashmap.values());
    }
}

// Method 2: Using character frequency as keys
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashmap = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26]; // Array to store character count
            for (char c : s.toCharArray()) {
                count[c - 'a']++; 
            }
            
            // Convert the character frequency array into a string key
            StringBuilder key = new StringBuilder();
            for (int num : count) {
                key.append(num).append("#"); // Unique delimiter to separate counts
            }
            
            hashmap.computeIfAbsent(key.toString(), k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(hashmap.values());
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

// Method 1: Using sorted strings as keys
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;

        for (string s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end()); // Sorting to check anagram validity
            hashmap[sorted_s].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& pair : hashmap) {
            ans.push_back(pair.second);
        }
        return ans;
    }
};

// Method 2: Using character frequency as keys
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;

        for (string s : strs) {
            vector<int> count(26, 0); // Array to store character count
            for (char c : s) {
                count[c - 'a']++; 
            }
            
            // Convert the character frequency array into a string key
            string key;
            for (int num : count) {
                key += to_string(num) + "#"; // Unique delimiter to separate counts
            }
            
            hashmap[key].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& pair : hashmap) {
            ans.push_back(pair.second);
        }
        return ans;
    }
};
"""