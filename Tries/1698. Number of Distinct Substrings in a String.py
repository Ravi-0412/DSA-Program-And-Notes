# method 1: 
# Brute Force
# logic: Take all substrings that can be generated from fixing an index. (same logic as GFG solution)
# and before adding any substring into ans check if that substring is already in the ans.
# Time: O(n^3) # There will be n^2 substrings and 'n' for checking each whether it is already in ans or not.
# space: O(n^3). There will be n^2 substrings and average length will be 'n/2'.

def countDistinctSubstrings(s):
    substrings = set()
    substrings.add("")  # Include the empty substring

    n = len(s)
    for i in range(n):
        curr = ""
        for j in range(i, n):
            curr += s[j]  # O(n) time to build substring
            if curr not in substrings:
                substrings.add(curr)

    return len(substrings)

# Java Code 
"""
import java.util.*;

public class Solution {
    public static int countDistinctSubstrings(String s) {
        Set<String> substrings = new HashSet<>();
        substrings.add("");  // Include the empty substring

        int n = s.length();
        for (int i = 0; i < n; i++) {
            String curr = "";
            for (int j = i; j < n; j++) {
                curr += s.charAt(j);  // O(n) time to build substring
                if (!substrings.contains(curr)) {
                    substrings.add(curr);
                }
            }
        }
        return substrings.size();
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int countDistinctSubstrings(const string& s) {
    unordered_set<string> substrings;
    substrings.insert("");  // Include the empty substring

    int n = s.length();
    for (int i = 0; i < n; ++i) {
        string curr = "";
        for (int j = i; j < n; ++j) {
            curr += s[j];  // O(n) time to build substring
            if (substrings.find(curr) == substrings.end()) {
                substrings.insert(curr);
            }
        }
    }
    return substrings.size();
}
"""

# method 2: 
# using Trie
# The basic intuition is to generate all the substrings and store them in the trie along with its creation. 
# If a substring already exists in the trie then we can ignore, else we can make an entry and increase the count.

# Jb kisi node pe split hoga means different substring otherwise already that substring mil chuka h.
# just logical is opposite of "Longest Common Prefix".

# time: O(n^2) . 
# space: can't be determined exactly but will be very less than O(n^3) in nature.

class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        
def countDistinctSubstrings(s):
    root= TrieNode()
    count= 1    # we have to include empty string also
    # just insert the substring starting from each index and if that is not present then incr the count else just incr the pointer.
    for i in range(len(s)):
        cur= root
        for j in range(i, len(s)):
            if s[j] not in cur.children:   # only need to insert s[j] since we are doing by Trie.
                # means found new different substring
                cur.children[s[j]]= TrieNode()
                count+= 1
            cur= cur.children[s[j]]
    return count

# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();  // will point to children. and can be max of 26('a' to 'z').
}

public class Solution {
    public static int countDistinctSubstrings(String s) {
        TrieNode root = new TrieNode();
        int count = 1;  // we have to include empty string also

        // just insert the substring starting from each index and if that is not present then incr the count else just incr the pointer.
        for (int i = 0; i < s.length(); i++) {
            TrieNode cur = root;
            for (int j = i; j < s.length(); j++) {
                char c = s.charAt(j);
                if (!cur.children.containsKey(c)) {  // only need to insert s[j] since we are doing by Trie.
                    // means found new different substring
                    cur.children.put(c, new TrieNode());
                    count++;
                }
                cur = cur.children.get(c);
            }
        }

        return count;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').
};

int countDistinctSubstrings(const string& s) {
    TrieNode* root = new TrieNode();
    int count = 1;  // we have to include empty string also

    // just insert the substring starting from each index and if that is not present then incr the count else just incr the pointer.
    for (int i = 0; i < s.length(); ++i) {
        TrieNode* cur = root;
        for (int j = i; j < s.length(); ++j) {
            char c = s[j];
            if (cur->children.find(c) == cur->children.end()) {  // only need to insert s[j] since we are doing by Trie.
                // means found new different substring
                cur->children[c] = new TrieNode();
                count++;
            }
            cur = cur->children[c];
        }
    }

    return count;
}
"""

# Extension: 

# Also printing all the distinct substring

def countDistinctSubstrings(s):
    root= TrieNode()
    count= 1    # we have to include empty string also
    ans= []    # will print all distinct substring except empty string. for empty string you can add that at 1st or last.
    for i in range(len(s)):
        curAns= ""
        cur= root
        for j in range(i, len(s)):
            curAns+= s[j]
            if s[j] not in cur.children:
                cur.children[s[j]]= TrieNode()
                count+= 1
                ans.append(curAns)
            cur= cur.children[s[j]]
    print(ans)
    return count

# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();  // will point to children. and can be max of 26('a' to 'z').
}

public class Solution {
    public static int countDistinctSubstrings(String s) {
        TrieNode root = new TrieNode();
        int count = 1;  // we have to include empty string also
        List<String> ans = new ArrayList<>();  // will print all distinct substrings except empty string

        for (int i = 0; i < s.length(); i++) {
            StringBuilder curAns = new StringBuilder();
            TrieNode cur = root;
            for (int j = i; j < s.length(); j++) {
                char c = s.charAt(j);
                curAns.append(c);
                if (!cur.children.containsKey(c)) {
                    cur.children.put(c, new TrieNode());  // means found new different substring
                    count++;
                    ans.add(curAns.toString());
                }
                cur = cur.children.get(c);
            }
        }

        System.out.println(ans);
        return count;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').
};

int countDistinctSubstrings(const string& s) {
    TrieNode* root = new TrieNode();
    int count = 1;  // we have to include empty string also
    vector<string> ans;  // will print all distinct substrings except empty string

    for (int i = 0; i < s.length(); ++i) {
        string curAns = "";
        TrieNode* cur = root;
        for (int j = i; j < s.length(); ++j) {
            char c = s[j];
            curAns += c;
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = new TrieNode();  // means found new different substring
                count++;
                ans.push_back(curAns);
            }
            cur = cur->children[c];
        }
    }

    for (const auto& substr : ans) {
        cout << substr << " ";
    }
    cout << endl;

    return count;
}
"""

# Note: 
# Q) why not directly applying the mathematical logical i.e  for a string of len 'n' no of total substring possible = (n*(n+1)) //2.
# how this formula: for len== 1 there will be 'n' substring, for len= 2->n-1 and so on for len= n ->1 ..
# so summatinon= (n*(n+1)) //2

# But this is only valid if all character in string is distinct .
# for e.g: s= "aaaa" 
# then our formula will give= 10
# Bt there will be only '4' distinct substring: a, aa, aaa, aaaa.


