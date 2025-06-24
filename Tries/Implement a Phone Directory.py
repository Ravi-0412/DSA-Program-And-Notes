# Method 1: 

# for every prefix in 'search_contact(qList)' , we have to return all contacts starting from that 'prefix'. 

class TrieNode:
    def __init__(self):
        self.children = {}         # Dictionary to hold child nodes for each character
        self.isEndOfWord = False   # True if the node marks the end of a contact

class Trie:
    def __init__(self):
        self.root = TrieNode()     # Root node of the Trie

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # If character is not present, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  # Move to the next node
        cur.isEndOfWord = True     # Mark the end of the word

class Solution:
    def displayContacts(self, n, contact, s):
        ans = []
        trie = Trie()

        # Insert all contacts into the Trie
        for word in set(contact):  # Use set to avoid duplicates
            trie.insert(word)

        prefix = ""
        pre = trie.root

        # For every character in query string 's'
        for c in s:
            # If prefix is not present in Trie, break and fill remaining with "0"
            if c not in pre.children:
                break
            prefix += c
            temp = []
            self.getSuggestions(pre.children[c], temp, prefix)
            ans.append(temp)
            pre = pre.children[c]

        # If no match found at any point, fill remaining results with ["0"]
        while len(ans) < len(s):
            ans.append(["0"])

        return ans

    def getSuggestions(self, cur, temp, prefix):
        # If a complete word ends at this node, add it to result list
        if cur.isEndOfWord:
            temp.append(prefix)
             # return            # because we can get the more words follwing the same path like tree.

        # Recursively search for all children nodes in lexicographical order
        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if char in cur.children:
                self.getSuggestions(cur.children[char], temp, prefix + char)

# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new TreeMap<>(); // Dictionary to hold child nodes for each character
    boolean isEndOfWord = false;                         // True if the node marks the end of a contact
}

class Trie {
    TrieNode root = new TrieNode(); // Root node of the Trie

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            // If character is not present, create a new TrieNode
            cur.children.putIfAbsent(c, new TrieNode());
            cur = cur.children.get(c); // Move to the next node
        }
        cur.isEndOfWord = true; // Mark the end of the word
    }
}

class Solution {
    public List<List<String>> displayContacts(int n, String[] contact, String s) {
        Trie trie = new Trie();
        List<List<String>> ans = new ArrayList<>();

        // Insert all contacts into the Trie (use TreeSet to avoid duplicates and sort)
        Set<String> uniqueContacts = new TreeSet<>(Arrays.asList(contact));
        for (String word : uniqueContacts) {
            trie.insert(word);
        }

        TrieNode pre = trie.root;
        String prefix = "";

        // For every character in query string 's'
        for (char c : s.toCharArray()) {
            if (!pre.children.containsKey(c)) {
                break; // If prefix is not present in Trie, break and fill remaining with "0"
            }
            prefix += c;
            List<String> temp = new ArrayList<>();
            getSuggestions(pre.children.get(c), temp, prefix);
            ans.add(temp);
            pre = pre.children.get(c);
        }

        // If no match found at any point, fill remaining results with ["0"]
        while (ans.size() < s.length()) {
            ans.add(Arrays.asList("0"));
        }

        return ans;
    }

    private void getSuggestions(TrieNode cur, List<String> temp, String prefix) {
        // If a complete word ends at this node, add it to result list
        if (cur.isEndOfWord) {
            temp.add(prefix);
        }
        // Recursively search for all children nodes in lexicographical order
        for (Map.Entry<Character, TrieNode> entry : cur.children.entrySet()) {
            getSuggestions(entry.getValue(), temp, prefix + entry.getKey());
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

class TrieNode {
public:
    map<char, TrieNode*> children; // Dictionary to hold child nodes for each character
    bool isEndOfWord = false;      // True if the node marks the end of a contact
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode(); // Root node of the Trie
    }

    void insert(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            // If character is not present, create a new TrieNode
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c]; // Move to the next node
        }
        cur->isEndOfWord = true; // Mark the end of the word
    }
};

class Solution {
public:
    vector<vector<string>> displayContacts(int n, vector<string>& contact, const string& s) {
        Trie trie;
        vector<vector<string>> ans;

        // Insert all contacts into the Trie (use set to avoid duplicates and sort)
        set<string> unique(contact.begin(), contact.end());
        for (const string& word : unique) {
            trie.insert(word);
        }

        TrieNode* pre = trie.root;
        string prefix = "";

        // For every character in query string 's'
        for (char c : s) {
            if (pre->children.find(c) == pre->children.end()) {
                break; // If prefix is not present in Trie, break and fill remaining with "0"
            }
            prefix += c;
            vector<string> temp;
            getSuggestions(pre->children[c], temp, prefix);
            ans.push_back(temp);
            pre = pre->children[c];
        }

        // If no match found at any point, fill remaining results with {"0"}
        while (ans.size() < s.size()) {
            ans.push_back({"0"});
        }

        return ans;
    }

    void getSuggestions(TrieNode* cur, vector<string>& temp, const string& prefix) {
        // If a complete word ends at this node, add it to result list
        if (cur->isEndOfWord) {
            temp.push_back(prefix);
        }

        // Recursively search for all children nodes in lexicographical order
        for (auto& [ch, node] : cur->children) {
            getSuggestions(node, temp, prefix + ch);
        }
    }
};
"""