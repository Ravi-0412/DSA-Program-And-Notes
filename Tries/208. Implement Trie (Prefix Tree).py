# Method 1: 

# Time complexity of all is O(n).

class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z'). just like data in linklist
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node. 
                                 # To diff between common node and node with ending word.

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root. just like 'head' of linklist
        
    def insert(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        # now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord= True

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return False
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur.isEndOfWord   # this is made 'True' to the child node of last char of the word.

    def startsWith(self, prefix: str) -> bool:
        cur= self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur= cur.children[c]
        # it means all char of prefix is present. so simply return True
        return True

"""
# Very short and another way of implementing tries in python
# https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python


T = lambda: defaultdict(T)
trie = T()
for w in forbidden:
    reduce(dict.__getitem__, w, trie)['#'] = True

# Meaning: 
# Will insert each word in tries 'trie' and mark the end of word by special symbol '#'.  => can you other symbol as well.

# See use here :
# https://leetcode.com/problems/length-of-the-longest-valid-substring/solutions/3771520/python-hashmap-and-trie-solutions/
"""

# Extension: 

"""
Note: we can use trie where we are sure that every number or ele or every word will be made only from a fixed thing like number or letter.
so that there is no need to create or check from scratch for every ele.
e.g: 
1) every word can be made only from letters 'a-z' i.e every ele in word will start from 'a-z' only. will have characters only from 'a-z'.
2) Every number when treated as Binary will have bit only '0' and '1'.
3) used in creating / searching word in dictionary
4) used to predict the possible word based on few typed words. e.g: Google Search Engine.
5) used to find the word 'starting with', 'Ending With' etc with a given substring.
6) used to find whether any word matches to already present word fully (that word exist) or partially(any prefix exist)
then we will use Trie if all word is made from same combination of characters.

"""

# Template to use in other Q.
# same as above just removed the comment.

class TrieNode:
    def __init__(self):
        self.children= {}  
        self.isEndOfWord= False   

class Trie:

    def __init__(self):
        self.root= TrieNode()   
        
    def insert(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur= cur.children[c]
        cur.isEndOfWord= True

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return False
            cur= cur.children[c]
        return cur.isEndOfWord   

# Other way : Using array of 26 instead of map in case of children
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # For 'a' to 'z'
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def _char_to_index(self, ch):
        return ord(ch) - ord('a')  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = self._char_to_index(c)
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            index = self._char_to_index(c)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            index = self._char_to_index(c)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return True  # Only checks if prefix path exists



# java Code
"""
import java.util.HashMap;

class TrieNode {
    public HashMap<Character, TrieNode> children;  // will point to children. and can be max of 26('a' to 'z'). just like data in linklist
    public boolean isEndOfWord;   // will mark True if that node is the last node of the word otherwise False for each node. 
                                  // To diff between common node and node with ending word.

    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class Trie {

    public TrieNode root;   // for every word, we will always start checking from root. just like 'head' of linklist

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                // insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children.put(c, new TrieNode());
            }
            // after inserting and if present already ,move cur to next child in both cases.
            cur = cur.children.get(c);
        }
        // now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return false;
            }
            cur = cur.children.get(c);
        }
        // now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur.isEndOfWord;   // this is made 'True' to the child node of last char of the word.
    }

    public boolean startsWith(String prefix) {
        TrieNode cur = root;
        for (char c : prefix.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return false;
            }
            cur = cur.children.get(c);
        }
        // it means all char of prefix is present. so simply return True
        return true;
    }
}
"""


# C++ code
"""
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z'). just like data in linklist
    bool isEndOfWord;   // will mark True if that node is the last node of the word otherwise False for each node. 
                        // To diff between common node and node with ending word.

    TrieNode() {
        isEndOfWord = false;
    }
};

class Trie {
public:
    TrieNode* root;   // for every word, we will always start checking from root. just like 'head' of linklist

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                // insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur->children[c] = new TrieNode();
            }
            // after inserting and if present already ,move cur to next child in both cases.
            cur = cur->children[c];
        }
        // now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }
            cur = cur->children[c];
        }
        // now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur->isEndOfWord;   // this is made 'True' to the child node of last char of the word.
    }

    bool startsWith(string prefix) {
        TrieNode* cur = root;
        for (char c : prefix) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }
            cur = cur->children[c];
        }
        // it means all char of prefix is present. so simply return True
        return true;
    }
};
"""
