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

# Java
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndOfWord;

    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

public class Trie {

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public String longestWord(String[] words) {
        // First, insert all the words into the Trie
        for (String word : words) {
            insert(word);
        }

        String longest = "";
        for (String word : words) {
            if (allPrefixesExist(word)) {
                if (word.length() > longest.length()) {
                    longest = word;
                } else if (word.length() == longest.length() && word.compareTo(longest) < 0) {
                    longest = word;
                }
            }
        }

        return longest.isEmpty() ? null : longest;
    }

    private void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }
        curr.isEndOfWord = true;
    }

    private boolean allPrefixesExist(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            curr = curr.children.get(c);
            if (curr == null || !curr.isEndOfWord) {
                return false;
            }
        }
        return true;
    }

    // Driver code
    public static void main(String[] args) {
        Trie T = new Trie();

        // String[] words = {"n", "ni", "nin", "ninj", "ninja", "ninga"};
        // String[] words = {"n", "ni", "nin", "ninj", "ninja", "ninga", "ninjas"};
        String[] words = {"np", "nhi", "nikn", "ninj"};
        // String[] words = {};

        String result = T.longestWord(words);
        System.out.println("Longest word with all prefixes is: " + result);
    }
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

# Java
#Method 1
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    String word;

    public TrieNode() {
        children = new HashMap<>();
        word = null;
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
            cur.children.putIfAbsent(c, new TrieNode());
            cur = cur.children.get(c);
        }
        cur.word = word; // Store the whole word at the end node
    }
}

public class Solution {

    public String longestWord(String[] words) {
        Trie trie = new Trie();

        // Insert all words into the Trie
        for (String word : words) {
            trie.insert(word);
        }

        String ans = "";
        Queue<TrieNode> q = new LinkedList<>();
        q.add(trie.root);

        while (!q.isEmpty()) {
            TrieNode cur = q.poll();
            for (TrieNode child : cur.children.values()) {
                if (child.word != null) {
                    // Update the answer if needed
                    if (child.word.length() > ans.length() || 
                        (child.word.length() == ans.length() && child.word.compareTo(ans) < 0)) {
                        ans = child.word;
                    }
                    q.add(child);
                }
            }
        }

        return ans.isEmpty() ? null : ans;
    }

    // Driver code
    public static void main(String[] args) {
        Solution sol = new Solution();
        // String[] words = {"n", "ni", "nin", "ninj", "ninja", "ninga"};
        // String[] words = {"n", "ni", "nin", "ninj", "ninja", "ninga", "ninjas"};
        String[] words = {"np", "nhi", "nikn", "ninj"};
        // String[] words = {};
        String result = sol.longestWord(words);
        System.out.println("Longest word with all prefixes is: " + result);
    }
}
"""
#Method 2
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    String word = null;
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur.children.putIfAbsent(c, new TrieNode());
            cur = cur.children.get(c);
        }
        cur.word = word;
    }
}

public class Solution {
    public String longestWord(List<String> words) {
        Trie trie = new Trie();
        for (String w : words) {
            trie.insert(w);
        }
        String ans = "";
        Queue<TrieNode> q = new LinkedList<>();
        q.offer(trie.root);

        while (!q.isEmpty()) {
            TrieNode cur = q.poll();
            for (TrieNode child : cur.children.values()) {
                if (child.word != null) {
                    if (child.word.length() > ans.length() || 
                        (child.word.length() == ans.length() && child.word.compareTo(ans) < 0)) {
                        ans = child.word;
                    }
                    q.offer(child);
                }
            }
        }
        return ans.equals("") ? null : ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<String> words = Arrays.asList("np", "nhi", "nikn", "ninj");
        System.out.println("longest word with all prefixes is: " + sol.longestWord(words));
    }
}

"""

# C++ Code 
#Method 1
"""
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord = false;
    TrieNode() {}
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
        cur->isEndOfWord = true;
    }

    bool ifAllPrefixExists(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            cur = cur->children[c];
            if (!cur->isEndOfWord) {
                return false;
            }
        }
        return true;
    }

    string LongestWord(const vector<string>& words) {
        // insert all words
        for (const auto& word : words) {
            insert(word);
        }
        string longest = "";
        for (const auto& word : words) {
            if (ifAllPrefixExists(word)) {
                if ((int)word.length() > (int)longest.length()) {
                    longest = word;
                } else if ((int)word.length() == (int)longest.length() && longest > word) {
                    longest = word;
                }
            }
        }
        return longest == "" ? "null" : longest;
    }
};

int main() {
    Trie T;
    vector<string> words = {"np", "nhi", "nikn", "ninj"};
    cout << "longest word with all prefixes is: " << T.LongestWord(words) << endl;
    return 0;
}

"""

#Method 2
"""
#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word = "";  // use empty string as None
    TrieNode() {}
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
        cur->word = word;  // store word at end node
    }
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        Trie trie;
        for (auto& w : words) {
            trie.insert(w);
        }

        string ans = "";
        queue<TrieNode*> q;
        q.push(trie.root);

        while (!q.empty()) {
            TrieNode* cur = q.front();
            q.pop();

            for (auto& [ch, child] : cur->children) {
                if (!child->word.empty()) {
                    if ((int)child->word.size() > (int)ans.size() || 
                        ((int)child->word.size() == (int)ans.size() && child->word < ans)) {
                        ans = child->word;
                    }
                    q.push(child);
                }
            }
        }
        return ans == "" ? "null" : ans;
    }
};

int main() {
    Solution sol;
    vector<string> words = {"np", "nhi", "nikn", "ninj"};
    cout << "longest word with all prefixes is: " << sol.longestWord(words) << endl;
    return 0;
}

"""
# Note: Try to do by find the ans by using dfs after inserting..Link in the sheet.

