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


# Java
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndOfWord;

    TrieNode() {
        children = new TreeMap<>();
        isEndOfWord = false;
    }
}

class Trie {
    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur.children.putIfAbsent(c, new TrieNode());
            cur = cur.children.get(c);
        }
        cur.isEndOfWord = true;
    }

    void getSuggestions(TrieNode node, List<String> temp, String prefix) {
        if (node.isEndOfWord) {
            temp.add(prefix);
        }
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            getSuggestions(entry.getValue(), temp, prefix + entry.getKey());
        }
    }
}

class Solution {
    public List<List<String>> displayContacts(int n, String[] contact, String s) {
        List<List<String>> ans = new ArrayList<>();
        Trie trie = new Trie();

        Set<String> contactSet = new HashSet<>(Arrays.asList(contact));
        for (String word : contactSet) {
            trie.insert(word);
        }

        TrieNode curr = trie.root;
        StringBuilder prefix = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (!curr.children.containsKey(c)) {
                while (ans.size() < s.length()) {
                    ans.add(Collections.singletonList("0"));
                }
                break;
            }

            prefix.append(c);
            curr = curr.children.get(c);
            List<String> temp = new ArrayList<>();
            trie.getSuggestions(curr, temp, prefix.toString());
            ans.add(temp);
        }

        while (ans.size() < s.length()) {
            ans.add(Collections.singletonList("0"));
        }

        return ans;
    }
}
"""
