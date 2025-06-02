"""
same way as we search but if there is '.' then we have to check all the possibility at that node, 
that case we have to check using dfs(backtrcaking).
"""

# for searching: 1st write the logic of normal search then for  dot  "." write recursion.

# Method 1:
class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        # now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord= True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    
    def dfs(self, word, ind, root):
        cur = root
        for i in range(ind, len(word)):
            c = word[i]
            if c!= '.':
                if c not in cur.children:
                    return False
                cur= cur.children[c]
            else:
                for child in cur.children.values():
                    if self.dfs(word, i+1, child):   # if any of one return True then no need to check other path.
                        return True
                # if neither of path return True then return False
                return False
        # now we are at last children node of the word
        return cur.isEndOfWord


# Method 2: 
# i thought like this.
class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()
        
    def addWord(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        # now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord= True
    
    def search(self, word: str) -> bool:

        def solve(word, root):
            # if not word:  # no need of this. last line will handle this automatically
            #     return root.isEndOfWord
            cur= root
            for i in range(len(word)):
                c= word[i]
                if c!= '.':
                    if c not in cur.children:
                        return False
                    cur= cur.children[c]
                else:
                    for num in range(97, 123):
                        ch= chr(num)
                        if ch in cur.children:
                            if solve(word[i+ 1: ], cur.children[ch]):
                                return True
                    return False  
            return cur.isEndOfWord

        return solve(word, self.root)
    

# Java
"""
// method 1:
# Here for children, we used array of TrieNode.

class TrieNode {
    public TrieNode[] children = new TrieNode[26]; // will point to children and can be max of 26 ('a' to 'z').
    public boolean isEndOfWord = false; // will mark true if that node is the last node of the word, otherwise false for each node.
}

public class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (cur.children[index] == null) {
                cur.children[index] = new TrieNode();
            }
            cur = cur.children[index];
        }
        cur.isEndOfWord = true; // now we have inserted all the chars of 'word', so make 'cur.isEndOfWord' true to denote the word ends at this node.
    }

    public boolean search(String word) {
        return dfs(word, 0, root);
    }

    private boolean dfs(String word, int ind, TrieNode root) {
        TrieNode cur = root;
        for (int i = ind; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c != '.') {
                int index = c - 'a';
                if (cur.children[index] == null) {
                    return false;
                }
                cur = cur.children[index];
            } else {
                for (TrieNode child : cur.children) {
                    if (child != null && dfs(word, i + 1, child)) { // if any of one returns true, then no need to check other paths.
                        return true;
                    }
                }
                // if neither of paths returns true, then return false
                return false;
            }
        }
        // now we are at last children node of the word
        return cur.isEndOfWord;
    }
}

"""
#Method 2 
"""
import java.util.HashMap;

class TrieNode {
    HashMap<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

public class WordDictionary {
    TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur.children.putIfAbsent(c, new TrieNode());
            cur = cur.children.get(c);
        }
        cur.isEndOfWord = true;
    }

    public boolean search(String word) {
        return solve(word, 0, root);
    }

    private boolean solve(String word, int index, TrieNode root) {
        TrieNode cur = root;
        for (int i = index; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c != '.') {
                if (!cur.children.containsKey(c)) {
                    return false;
                }
                cur = cur.children.get(c);
            } else {
                // If '.' try all children 'a' to 'z'
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    if (cur.children.containsKey(ch)) {
                        if (solve(word, i + 1, cur.children.get(ch))) {
                            return true;
                        }
                    }
                }
                return false;
            }
        }
        return cur.isEndOfWord;
    }
}

"""


#C++ Code
#Method 1
"""
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').
    bool isEndOfWord = false;  // will mark True if that node is the last node of the word otherwise False for each node.

    TrieNode() {}
};

class WordDictionary {
public:
    TrieNode* root;

    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = new TrieNode();
            }
            // after inserting and if present already, move cur to next child in both cases.
            cur = cur->children[c];
        }
        // now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur->isEndOfWord = true;
    }

    bool search(string word) {
        return dfs(word, 0, root);
    }

private:
    bool dfs(const string& word, int ind, TrieNode* root) {
        TrieNode* cur = root;
        for (int i = ind; i < (int)word.size(); i++) {
            char c = word[i];
            if (c != '.') {
                if (cur->children.find(c) == cur->children.end()) {
                    return false;
                }
                cur = cur->children[c];
            } else {
                // if c is '.', we need to check all possible children
                for (auto& childPair : cur->children) {
                    TrieNode* child = childPair.second;
                    if (dfs(word, i + 1, child)) {  // if any one return True then no need to check other path.
                        return true;
                    }
                }
                // if neither of path return True then return False
                return false;
            }
        }
        // now we are at last children node of the word
        return cur->isEndOfWord;
    }
};

"""
#Method 2 
"""
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // max 26 letters
    bool isEndOfWord = false;

    TrieNode() {}
};

class WordDictionary {
public:
    TrieNode* root;

    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
        }
        cur->isEndOfWord = true;
    }

    bool search(string word) {
        return solve(word, 0, root);
    }

private:
    // Recursive helper function simulating the Python solve with substring slicing replaced by index.
    bool solve(const string& word, int index, TrieNode* root) {
        TrieNode* cur = root;
        for (int i = index; i < (int)word.size(); i++) {
            char c = word[i];
            if (c != '.') {
                if (cur->children.find(c) == cur->children.end()) {
                    return false;
                }
                cur = cur->children[c];
            } else {
                // For '.', try all children (a-z)
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    if (cur->children.find(ch) != cur->children.end()) {
                        if (solve(word, i + 1, cur->children[ch])) {
                            return true;
                        }
                    }
                }
                return false;
            }
        }
        return cur->isEndOfWord;
    }
};

"""
