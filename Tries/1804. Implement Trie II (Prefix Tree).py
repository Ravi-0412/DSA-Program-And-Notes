# little bit modified the functions to get the ans easily.
# just same logic only

# Note: we are updating 'word_count' and 'prefix_count' after each node like 'isEndOfWord'.

# submitted on codingninja.
class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.word_count= 0     # will tell the frequency of word. (node at which we were marking 'isEndOfWord= True', there we will increase this count)
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
            cur= cur.children[c]
            # After inserting node increase its prefix_count
            cur.prefix_count+= 1
        # now increase the word_count for this node.
        # cur.prefix_count+= 1  # we have already updated prefix_count for this node loop itself.
        cur.word_count+= 1

    def countWordsEqualTo(self, word):
        node= self.search(word)
        return 0 if node== None else node.word_count
    
    def countWordsStartingWith(self, prefix: str) -> bool:
        node= self.search(prefix)
        return 0 if node== None else node.prefix_count
    
    # for erasing the word, just decr the count of each prefix and count of word itself.
    def erase(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
            cur.prefix_count-= 1
        # cur.prefix_count-= 1    # we have already updated prefix_count for this node loop itself.
        cur.word_count-= 1

    # A node has more than one variable or ans(wordCount or prefixCount) so just return 'node' itself because we don't know what ans we will have to return from this node.

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return None
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur


# another way
class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.prefixes= [0, 0]  # 1st : will tell no of word ending at that node and if =0 means no word end at that node.and
                               # 2nd:  will tell no of word which has this prefix and if =0 means no prefix at that node.
                # just took prefixes instead of 'isEndOfWord'                      
class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            cur= cur.children[c]
            # After inserting node increase its prefix_count
            cur.prefixes[1]+= 1
        # now increase the word_count for this node.
        cur.prefixes[0]+= 1

    def countWordsEqualTo(self, word):
        node= self.search(word)
        return 0 if node== None else node.prefixes[0]
    
    def countWordsStartingWith(self, prefix: str) -> bool:
        node= self.search(prefix)
        return 0 if node== None else node.prefixes[1]
    
    # for erasing the word, just decr the count of each prefix and count of word itself.
    def erase(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
            cur.prefixes[1]-= 1
        cur.prefixes[0]-= 1

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return None
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur
    

# Note: whenever you have to remove any word apply the prefix_count with isEndofWord(or word_count).
# while adding incr the count of both and while removing decr the count.

#Java Code
"""
//Method 1
import java.util.HashMap;
import java.util.Map;

class TrieNode {
    Map<Character, TrieNode> children;   // will point to children. and can be max of 26('a' to 'z').
    int word_count;     // will tell the frequency of word. (node at which we were marking 'isEndOfWord= True', there we will increase this count)
    int prefix_count;   // will tell no of word staring with a given prefix. after every node you are inserting increase this count.

    public TrieNode() {
        children = new HashMap<>();
        word_count = 0;
        prefix_count = 0;
    }
}

class Trie {

    TrieNode root;

    public Trie() {
        root = new TrieNode();   // for every word, we will always start checking from root.
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                // insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
            // After inserting node increase its prefix_count
            cur.prefix_count += 1;
        }
        // now increase the word_count for this node.
        // cur.prefix_count+= 1;  // we have already updated prefix_count for this node loop itself.
        cur.word_count += 1;
    }

    public int countWordsEqualTo(String word) {
        TrieNode node = search(word);
        return node == null ? 0 : node.word_count;
    }

    public int countWordsStartingWith(String prefix) {
        TrieNode node = search(prefix);
        return node == null ? 0 : node.prefix_count;
    }

    // for erasing the word, just decr the count of each prefix and count of word itself.
    public void erase(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur = cur.children.get(c);
            cur.prefix_count -= 1;
        }
        // cur.prefix_count-= 1;    // we have already updated prefix_count for this node loop itself.
        cur.word_count -= 1;
    }

    // A node has more than one variable or ans(wordCount or prefixCount) so just return 'node' itself because we don't know what ans we will have to return from this node.
    public TrieNode search(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return null;
            }
            cur = cur.children.get(c);
        }
        // now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur;
    }
}


//Method 2
import java.util.HashMap;
import java.util.Map;

class TrieNode {
    Map<Character, TrieNode> children;  // will point to children. and can be max of 26('a' to 'z').
    int[] prefixes;  // 1st : will tell no of word ending at that node and if =0 means no word end at that node.and
                     // 2nd:  will tell no of word which has this prefix and if =0 means no prefix at that node.
                     // just took prefixes instead of 'isEndOfWord'

    public TrieNode() {
        children = new HashMap<>();
        prefixes = new int[2];
    }
}

class Trie {

    TrieNode root;

    public Trie() {
        root = new TrieNode();   // for every word, we will always start checking from root.
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                // insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
            // After inserting node increase its prefix_count
            cur.prefixes[1] += 1;
        }
        // now increase the word_count for this node.
        cur.prefixes[0] += 1;
    }

    public int countWordsEqualTo(String word) {
        TrieNode node = search(word);
        return node == null ? 0 : node.prefixes[0];
    }

    public int countWordsStartingWith(String prefix) {
        TrieNode node = search(prefix);
        return node == null ? 0 : node.prefixes[1];
    }

    // for erasing the word, just decr the count of each prefix and count of word itself.
    public void erase(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur = cur.children.get(c);
            cur.prefixes[1] -= 1;
        }
        cur.prefixes[0] -= 1;
    }

    public TrieNode search(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return null;
            }
            cur = cur.children.get(c);
        }
        // now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur;
    }
}

"""

#C++ Code 
"""
//Method 1
#include <unordered_map>
#include <string>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').
    int word_count;     // will tell the frequency of word. (node at which we were marking 'isEndOfWord= True', there we will increase this count)
    int prefix_count;   // will tell no of word staring with a given prefix. after every node you are inserting increase this count.

    TrieNode() {
        word_count = 0;
        prefix_count = 0;
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();   // for every word, we will always start checking from root.
    }

    void insert(const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                // insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
            // After inserting node increase its prefix_count
            cur->prefix_count += 1;
        }
        // now increase the word_count for this node.
        // cur.prefix_count+= 1;  // we have already updated prefix_count for this node loop itself.
        cur->word_count += 1;
    }

    TrieNode* search(const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                return nullptr;
            }
            cur = cur->children[c];
        }
        // now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur;
    }

    int countWordsEqualTo(const std::string& word) {
        TrieNode* node = search(word);
        return node == nullptr ? 0 : node->word_count;
    }

    int countWordsStartingWith(const std::string& prefix) {
        TrieNode* node = search(prefix);
        return node == nullptr ? 0 : node->prefix_count;
    }

    // for erasing the word, just decr the count of each prefix and count of word itself.
    void erase(const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            cur = cur->children[c];
            cur->prefix_count -= 1;
        }
        // cur.prefix_count-= 1;    // we have already updated prefix_count for this node loop itself.
        cur->word_count -= 1;
    }
};

//Method 2
#include <unordered_map>
#include <string>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').
    int prefixes[2];  // 1st : will tell no of word ending at that node and if =0 means no word end at that node.and
                      // 2nd:  will tell no of word which has this prefix and if =0 means no prefix at that node.
                      // just took prefixes instead of 'isEndOfWord'

    TrieNode() {
        prefixes[0] = 0;
        prefixes[1] = 0;
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();   // for every word, we will always start checking from root.
    }

    void insert(const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                // insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
            // After inserting node increase its prefix_count
            cur->prefixes[1] += 1;
        }
        // now increase the word_count for this node.
        cur->prefixes[0] += 1;
    }

    TrieNode* search(const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                return nullptr;
            }
            cur = cur->children[c];
        }
        // now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur;
    }

    int countWordsEqualTo(const std::string& word) {
        TrieNode* node = search(word);
        return node == nullptr ? 0 : node->prefixes[0];
    }

    int countWordsStartingWith(const std::string& prefix) {
        TrieNode* node = search(prefix);
        return node == nullptr ? 0 : node->prefixes[1];
    }

    // for erasing the word, just decr the count of each prefix and count of word itself.
    void erase(const std::string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            cur = cur->children[c];
            cur->prefixes[1] -= 1;
        }
        cur->prefixes[0] -= 1;
    }
};

"""