# Method 1: Brute force
"""
Time Complexity: 
O(n * m)
(n) is the number of words in the array.
(m) is the average length of each word.
For each word, checking the prefix using startswith() takes (O(m)) time.
"""

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

# Java
"""
class Solution {
    public int prefixCount(String[] words, String pref) {
        int count = 0;
        for (String word : words) {
            if (word.startsWith(pref)) {
                count++;
            }
        }
        return count;
    }
}
"""

# Method 2: Using Trie
# Just used same code of: "211. Design Add and Search Words Data Structure"

# Time: Same as above only

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.countWordsStartingWith(pref)

class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.prefix_count= 0   # will tell no of word staring with a given prefix. after every node you are inserting increase this count.

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            cur = cur.children[c]
            # After inserting node increase its prefix_count
            cur.prefix_count += 1
    
    def countWordsStartingWith(self, prefix: str) -> bool:
        node = self.search(prefix)
        return 0 if node == None else node.prefix_count

    # A node has more than one variable or ans(wordCount or prefixCount) so just return 'node' itself because we don't know what ans we will    have to return from this node.

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur

# Java
"""
import java.util.*;

class Solution {
    public int prefixCount(String[] words, String pref) {
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }
        return trie.countWordsStartingWith(pref);
    }
}

class TrieNode {
    Map<Character, TrieNode> children;
    int prefixCount;

    public TrieNode() {
        children = new HashMap<>();
        prefixCount = 0;
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
            cur.prefixCount++;
        }
    }

    public int countWordsStartingWith(String prefix) {
        TrieNode node = search(prefix);
        return node == null ? 0 : node.prefixCount;
    }

    public TrieNode search(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return null;
            }
            cur = cur.children.get(c);
        }
        return cur;
    }
}
"""
