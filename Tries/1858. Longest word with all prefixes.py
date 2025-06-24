# Method 1: 

"""
why Trie?
We have to check all prefixes of a word is is present in the array or not.
Higher length prefix will form by adding one letter(last one) to the just previous prefix.
so we are getting all prefix by adding one letter to the already existing prefix(word).

So if we insert all the given words and check for each word whether all its prefixes has 'isEndOfWord= True' or not.
Since we have to check all its prefix so best data structure is Trie.

So first insert all the words in the Trie and check for each word whether all its prefixes has 'isEndOfWord= True'.

Note: Q in other words : "Given array of string and given another word . Check whether all the prefixes of this present in the array or not".
we will do the same thing .

Time: O(N * M), where N is length of words, M  is length of each word.
Space: O(N * M)
"""

class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').   (just like 'next' in linklist)
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
    
    def LongestWord(self, words):
        # First insert all the words in the Trie
        for word in words:
            self.insert(word)

        # now traverse each word and find the ans if all the prefix of word exists.
        longest= ""
        for word in words:
            if self.ifAllPrefixExists(word):
                if len(word) > len(longest):
                    longest= word
                elif len(word)== len(longest) and longest > word :  # when length is same, we have to take the word alphabetically small.
                    longest= word
        return None if longest== "" else longest

    # Exactly same as we insert
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

    # just exactly same as we search just checking whether all its prefixes i.e all nodes with char of word has 'isEndOfWord= True' or not.
    def ifAllPrefixExists(self, word):  
        cur= self.root
        for c in word:
            cur= cur.children[c]
            if cur.isEndOfWord== False:  
                return False
        return True

T= Trie()
# words= ["n", "ni", "nin", "ninj", "ninja", "ninga"]
# words= ["n", "ni", "nin", "ninj", "ninja", "ninga", "ninjas"]
words= ["np", "nhi", "nikn", "ninj"]
# words= []
print("longest word with all prefixes is: ", T.LongestWord(words))

# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();  // will point to children. and can be max of 26('a' to 'z').   (just like 'next' in linklist)
    boolean isEndOfWord = false;  // will mark True if that node is the last node of the word otherwise False for each node.
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();  // for every word, we will always start checking from root.
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                // insert 'c' into children and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children.put(c, new TrieNode());
            }
            // after inserting and if present already, move cur to next child in both cases.
            cur = cur.children.get(c);
        }
        // now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord = true;
    }

    public boolean ifAllPrefixExists(String word) {
        // just exactly same as we search just checking whether all its prefixes i.e all nodes with char of word has 'isEndOfWord= True' or not.
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur = cur.children.get(c);
            if (cur == null || !cur.isEndOfWord) {
                return false;
            }
        }
        return true;
    }

    public String LongestWord(String[] words) {
        for (String word : words) {
            insert(word);  // First insert all the words in the Trie
        }

        String longest = "";
        // now traverse each word and find the ans if all the prefix of word exists.
        for (String word : words) {
            if (ifAllPrefixExists(word)) {
                if (word.length() > longest.length()) {
                    longest = word;
                } else if (word.length() == longest.length() && word.compareTo(longest) < 0) {
                    // when length is same, we have to take the word alphabetically small.
                    longest = word;
                }
            }
        }
        return longest.equals("") ? null : longest;
    }
}

public class Main {
    public static void main(String[] args) {
        Trie T = new Trie();
        String[] words = {"np", "nhi", "nikn", "ninj"};
        System.out.println("longest word with all prefixes is: " + T.LongestWord(words));
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').   (just like 'next' in linklist)
    bool isEndOfWord = false;  // will mark True if that node is the last node of the word otherwise False for each node.
};

class Trie {
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();  // for every word, we will always start checking from root.
    }

    void insert(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                // insert 'c' into children and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur->children[c] = new TrieNode();
            }
            // after inserting and if present already, move cur to next child in both cases.
            cur = cur->children[c];
        }
        // now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur->isEndOfWord = true;
    }

    bool ifAllPrefixExists(const string& word) {
        // just exactly same as we search just checking whether all its prefixes i.e all nodes with char of word has 'isEndOfWord= True' or not.
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end() || !cur->children[c]->isEndOfWord)
                return false;
            cur = cur->children[c];
        }
        return true;
    }

    string LongestWord(const vector<string>& words) {
        for (const string& word : words) {
            insert(word);  // First insert all the words in the Trie
        }

        string longest = "";
        // now traverse each word and find the ans if all the prefix of word exists.
        for (const string& word : words) {
            if (ifAllPrefixExists(word)) {
                if (word.length() > longest.length()) {
                    longest = word;
                } else if (word.length() == longest.length() && word < longest) {
                    // when length is same, we have to take the word alphabetically small.
                    longest = word;
                }
            }
        }
        return longest.empty() ? "None" : longest;
    }
};

int main() {
    Trie T;
    vector<string> words = {"np", "nhi", "nikn", "ninj"};
    cout << "longest word with all prefixes is: " << T.LongestWord(words) << endl;
    return 0;
}
"""

# method 2:
# very good and concise
class TrieNode:
    def __init__(self):
        self.children= {}  
        self.word= None

class Trie:
    def __init__(self):
        self.root= TrieNode()
    
    def insert(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            cur= cur.children[c]
        cur.word= word  # put the word to check the word directly.

class Solution:
    
    def longestWord(self, words):
        trie = Trie()
        # First insert all the words in the Trie
        for word in words:
            trie.insert(word)
        
        ans = ""
        q = collections.deque([])
        q.append(trie.root)  # will only contain the node that will have same ending word except root since we update all the things in next node.

        while q:
            cur = q.popleft()
            for child in cur.children.values():
                if child.word:  # means this node contain some ending word.
                    if len(child.word) > len(ans) or (len(child.word) == len(ans) and child.word < ans):
                        ans= child.word
                    q.append(child)
        return None if ans== "" else ans


# Java Code 
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();  // will point to children. and can be max of 26('a' to 'z'). (just like 'next' in linklist)
    String word = null;  // will store the word at the end node.
}

class Trie {
    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
        }
        cur.word = word;  // put the word to check the word directly.
    }
}

class Solution {
    public String longestWord(String[] words) {
        Trie trie = new Trie();
        // First insert all the words in the Trie
        for (String word : words) {
            trie.insert(word);
        }

        String ans = "";
        Deque<TrieNode> q = new ArrayDeque<>();
        q.add(trie.root);  // will only contain the node that will have same ending word except root since we update all the things in next node.

        while (!q.isEmpty()) {
            TrieNode cur = q.poll();
            for (TrieNode child : cur.children.values()) {
                if (child.word != null) {  // means this node contain some ending word.
                    if (child.word.length() > ans.length() || 
                       (child.word.length() == ans.length() && child.word.compareTo(ans) < 0)) {
                        ans = child.word;
                    }
                    q.add(child);
                }
            }
        }
        return ans.equals("") ? null : ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <queue>
#include <string>
#include <vector>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z'). (just like 'next' in linklist)
    string word;  // will store the word at the end node.

    TrieNode() {
        word = "";
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
        }
        cur->word = word;  // put the word to check the word directly.
    }
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        Trie trie;
        // First insert all the words in the Trie
        for (const string& word : words) {
            trie.insert(word);
        }

        string ans = "";
        queue<TrieNode*> q;
        q.push(trie.root);  // will only contain the node that will have same ending word except root since we update all the things in next node.

        while (!q.empty()) {
            TrieNode* cur = q.front();
            q.pop();
            for (auto& p : cur->children) {
                TrieNode* child = p.second;
                if (!child->word.empty()) {  // means this node contain some ending word.
                    if (child->word.length() > ans.length() ||
                       (child->word.length() == ans.length() && child->word < ans)) {
                        ans = child->word;
                    }
                    q.push(child);
                }
            }
        }
        return ans == "" ? "None" : ans;
    }
};
"""