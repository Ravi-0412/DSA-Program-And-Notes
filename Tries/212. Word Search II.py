
# getting TLE using the logic of 'word search 1' i.e serarching the word one by one.
# time: O(w.m*n.4^(m*n))  , w: # words

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans= []
        for word in words:
            print(word,"word")
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.dfs(board, i, j, word):
                        ans.append(word)
        return list(set(ans))   # we can get duplicate of same word if any word can be formed from more than one way.

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

# method 2: 
# we can optimise the above problem to O(m*n.4^(m*n)) + O(n) (for inserting all words into Trie).
# logic: First insert all words into the Trie.
# search from each cell in the matrix only one time. (here we are searching from each cell only one time not 'w' time for each word)
# And if we find any word then add into the ans.

# i.e we are checking from each cell what  all words we can form starting from that cell.

# We are removing the 'word' from the trie after we have found that to reduce the time complexity.
# since we only need only distinct word. 
# This will little bit optimise the time since we won't be checking same word again following other path.

# and there are chances that we can get the same word(by following other path in grid). so storing ans in set first.
# vvi: But when we are removing the word after finding that word then no way we can get that word again so we can store
# ans directly in list only.

# Removing the word will optimise the time little bit. 

# Note: we are not returning after getting any word or after function call since we can get other word also following the link.


class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.isWord= False

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        # now increase the word_count for this node.
        cur.isWord= True
    
    # Mark 'isWord= False' so we won't check again.
    def removeWord(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
        cur.isWord= False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert all words into Trie.
        trie= Trie()
        for word in words:
            trie.insert(word)

        # now start searching from each cell.
        rows, cols= len(board), len(board[0])
        ans = set()  # storing in set since same word can be formed from more than one cell as starting node.
        visited = set()  # to check if we have already visited any cell.
        
        def dfs(r, c, node, word):
            # write all the invalid possible cases together.
            if r <0 or r== rows or c < 0 or c== cols or (r,c) in visited or board[r][c] not in node.children :
                return 
            word += board[r][c]
            visited.add((r,c))
            node= node.children[board[r][c]]
            # we can get any matching word anytime so keep checking after each node.
            if node.isWord:
                ans.add(word)
                trie.removeWord(word)
            # visit all the four possible directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            # now backtrack
            visited.remove((r, c))
        
        # # now start searching from each cell.
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie.root, "")

        return list(ans)
        

# Method 3: my way (just same we did word search 1)

class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.isWord= False

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        cur.isWord= True
    
    def removeWord(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
            cur.prefix_count-= 1
        cur.isWord= False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # insert all words into Trie.
        trie= Trie()
        for word in words:
            trie.insert(word)

        # now start searching from each cell.
        rows, cols= len(board), len(board[0])
        ans= set()  # storing in set since same word can be formed from more than one cell as starting node.
        
        def dfs(r, c, node, word):
            node= node.children[board[r][c]]
            # we can get any matching word anytime so keep checking after each node.
            if node.isWord:  # in next node we are updating everything so we will check in next node only.
                ans.add(word)
                trie.removeWord(word)
            
            temp= board[r][c]
            board[r][c]= "#"  # marking visited
            # visit all the four possible directions
            directions= [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]
            for nr, nc in directions:
                if 0<=nr < rows and 0<= nc < cols and board[nr][nc]!= "#" and board[nr][nc] in  node.children : 
                    dfs(nr, nc, node, word + board[nr][nc])
            # now backtrack if we don't ans by adding the char at (r,c)
            board[r][c]= temp
        
        # # now start searching from each cell.
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root, board[r][c])

        return list(ans)



# Java Code
# Method 1
"""
import java.util.*;

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        List<String> ans = new ArrayList<>();
        for (String word : words) {
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    if (dfs(board, i, j, word)) {
                        ans.add(word);
                        break;  // No need to continue once word is found
                    }
                }
            }
        }
        // remove duplicates by converting to a set and back to list
        return new ArrayList<>(new HashSet<>(ans));
    }

    private boolean dfs(char[][] board, int i, int j, String word) {
        if (word.length() == 0) // all characters checked
            return true;
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(0))
            return false;

        char tmp = board[i][j];  // first char found, check remaining
        board[i][j] = '#';       // mark visited
        String nextWord = word.substring(1);
        boolean res = dfs(board, i + 1, j, nextWord) || 
                      dfs(board, i - 1, j, nextWord) || 
                      dfs(board, i, j + 1, nextWord) || 
                      dfs(board, i, j - 1, nextWord);
        board[i][j] = tmp;       // backtrack
        return res;
    }
}
"""
#Method 2
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();  // will point to children. and can be max of 26('a' to 'z').
    boolean isWord = false;
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
                // insert 'c' into children and make 'c' point to a TrieNode and move cur to next child (just added one)
                cur.children.put(c, new TrieNode());
            }
            // after inserting and if present already, move cur to next child in both cases.
            cur = cur.children.get(c);
        }
        // now mark this node as word end.
        cur.isWord = true;
    }

    // Mark 'isWord= False' so we won't check again.
    public void removeWord(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur = cur.children.get(c);
        }
        cur.isWord = false;
    }
}

public class Solution {
    int rows, cols;
    Set<String> ans;
    char[][] board;
    Trie trie;
    boolean[][] visited;

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        rows = board.length;
        cols = board[0].length;
        trie = new Trie();

        // insert all words into Trie.
        for (String word : words) {
            trie.insert(word);
        }

        ans = new HashSet<>();  // storing in set since same word can be formed from more than one cell as starting node.
        visited = new boolean[rows][cols];  // to check if we have already visited any cell.

        // now start searching from each cell.
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                dfs(r, c, trie.root, "");
            }
        }

        return new ArrayList<>(ans);
    }

    private void dfs(int r, int c, TrieNode node, String word) {
        // write all the invalid possible cases together.
        if (r < 0 || r >= rows || c < 0 || c >= cols || visited[r][c] || !node.children.containsKey(board[r][c])) {
            return;
        }

        word += board[r][c];
        visited[r][c] = true;
        node = node.children.get(board[r][c]);

        // we can get any matching word anytime so keep checking after each node.
        if (node.isWord) {
            ans.add(word);
            trie.removeWord(word);
        }

        // visit all the four possible directions
        dfs(r + 1, c, node, word);
        dfs(r - 1, c, node, word);
        dfs(r, c + 1, node, word);
        dfs(r, c - 1, node, word);

        // now backtrack
        visited[r][c] = false;
    }
}

"""
#Method 3
"""
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();  // will point to children. and can be max of 26('a' to 'z').
    boolean isWord = false;
    // int prefix_count; // Not used here as in your Python code prefix_count decrement is done but not declared
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
                // insert 'c' into children and make 'c' point to a TrieNode and move curr to next child (just added one)
                cur.children.put(c, new TrieNode());
            }
            // after inserting and if present already ,move cur to next child in both cases.
            cur = cur.children.get(c);
        }
        cur.isWord = true;
    }

    public void removeWord(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            cur = cur.children.get(c);
            // In Python you do cur.prefix_count -= 1, but prefix_count is never defined or used. Skip here.
        }
        cur.isWord = false;
    }
}

public class Solution {
    int rows, cols;
    Set<String> ans;
    char[][] board;
    Trie trie;

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        rows = board.length;
        cols = board[0].length;
        trie = new Trie();

        // insert all words into Trie.
        for (String word : words) {
            trie.insert(word);
        }

        ans = new HashSet<>();  // storing in set since same word can be formed from more than one cell as starting node.

        // now start searching from each cell.
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (trie.root.children.containsKey(board[r][c])) {
                    dfs(r, c, trie.root, "" + board[r][c]);
                }
            }
        }

        return new ArrayList<>(ans);
    }

    private void dfs(int r, int c, TrieNode node, String word) {
        node = node.children.get(board[r][c]);
        // we can get any matching word anytime so keep checking after each node.
        if (node.isWord) {  // in next node we are updating everything so we will check in next node only.
            ans.add(word);
            trie.removeWord(word);
        }

        char temp = board[r][c];
        board[r][c] = '#';  // marking visited

        // visit all the four possible directions
        int[][] directions = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}};
        for (int[] dir : directions) {
            int nr = dir[0], nc = dir[1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                    && board[nr][nc] != '#' && node.children.containsKey(board[nr][nc])) {
                dfs(nr, nc, node, word + board[nr][nc]);
            }
        }

        // now backtrack if we don't ans by adding the char at (r,c)
        board[r][c] = temp;
    }
}

"""

##C++ Code
#Method 1
"""
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> ans;
        for (const string& word : words) {
            bool found = false;
            for (int i = 0; i < board.size() && !found; i++) {
                for (int j = 0; j < board[0].size() && !found; j++) {
                    if (dfs(board, i, j, word)) {
                        ans.push_back(word);
                        found = true;  // once found, stop searching for this word
                    }
                }
            }
        }
        // remove duplicates by inserting into a set and back to vector
        unordered_set<string> seen(ans.begin(), ans.end());
        return vector<string>(seen.begin(), seen.end());
    }

private:
    bool dfs(vector<vector<char>>& board, int i, int j, const string& word) {
        if (word.size() == 0) return true;  // all characters matched
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[0])
            return false;

        char tmp = board[i][j];
        board[i][j] = '#';  // mark as visited
        string nextWord = word.substr(1);
        bool res = dfs(board, i + 1, j, nextWord) ||
                   dfs(board, i - 1, j, nextWord) ||
                   dfs(board, i, j + 1, nextWord) ||
                   dfs(board, i, j - 1, nextWord);
        board[i][j] = tmp;  // backtrack
        return res;
    }
};

"""

#Method 2
"""
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;  // will point to children. and can be max of 26('a' to 'z').
    bool isWord;

    TrieNode() {
        isWord = false;
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();   // for every word, we will always start checking from root.
    }

    void insert(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                // insert 'c' into children and make 'c' point to a TrieNode and move cur to next child (just added one)
                cur->children[c] = new TrieNode();
            }
            // after inserting and if present already, move cur to next child in both cases.
            cur = cur->children[c];
        }
        // now mark this node as word end.
        cur->isWord = true;
    }

    // Mark 'isWord= False' so we won't check again.
    void removeWord(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            cur = cur->children[c];
        }
        cur->isWord = false;
    }
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // insert all words into Trie.
        Trie trie;
        for (const string& word : words) {
            trie.insert(word);
        }

        int rows = board.size();
        int cols = board[0].size();

        unordered_set<string> ans;  // storing in set since same word can be formed from more than one cell as starting node.
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));  // to check if we have already visited any cell.

        function<void(int, int, TrieNode*, string)> dfs = [&](int r, int c, TrieNode* node, string word) {
            // write all the invalid possible cases together.
            if (r < 0 || r == rows || c < 0 || c == cols || visited[r][c] || node->children.find(board[r][c]) == node->children.end()) {
                return;
            }

            word += board[r][c];
            visited[r][c] = true;
            node = node->children[board[r][c]];

            // we can get any matching word anytime so keep checking after each node.
            if (node->isWord) {
                ans.insert(word);
                trie.removeWord(word);
            }

            // visit all the four possible directions
            dfs(r + 1, c, node, word);
            dfs(r - 1, c, node, word);
            dfs(r, c + 1, node, word);
            dfs(r, c - 1, node, word);

            // now backtrack
            visited[r][c] = false;
        };

        // now start searching from each cell.
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                dfs(r, c, trie.root, "");
            }
        }

        return vector<string>(ans.begin(), ans.end());
    }
};

"""
#Method 3
"""
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children; // will point to children. and can be max of 26('a' to 'z').
    bool isWord = false;
    // int prefix_count; // Not used here, skipped as in Python code

    TrieNode() {}
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();  // for every word, we will always start checking from root.
    }

    void insert(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                // insert 'c' into children and make 'c' point to a TrieNode and move curr to next child (just added one)
                cur->children[c] = new TrieNode();
            }
            // after inserting and if present already ,move cur to next child in both cases.
            cur = cur->children[c];
        }
        cur->isWord = true;
    }

    void removeWord(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            cur = cur->children[c];
            // cur->prefix_count -= 1; // not used, skipping
        }
        cur->isWord = false;
    }
};

class Solution {
    int rows, cols;
    unordered_set<string> ans;
    vector<vector<char>> board;
    Trie trie;

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        this->board = board;
        rows = board.size();
        cols = board[0].size();

        // insert all words into Trie.
        for (auto& word : words) {
            trie.insert(word);
        }

        // storing in set since same word can be formed from more than one cell as starting node.
        ans.clear();

        // now start searching from each cell.
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (trie.root->children.find(board[r][c]) != trie.root->children.end()) {
                    dfs(r, c, trie.root, string(1, board[r][c]));
                }
            }
        }

        // convert set to vector
        return vector<string>(ans.begin(), ans.end());
    }

private:
    void dfs(int r, int c, TrieNode* node, string word) {
        node = node->children[board[r][c]];
        // we can get any matching word anytime so keep checking after each node.
        if (node->isWord) {  // in next node we are updating everything so we will check in next node only.
            ans.insert(word);
            trie.removeWord(word);
        }

        char temp = board[r][c];
        board[r][c] = '#';  // marking visited

        // visit all the four possible directions
        int directions[4][2] = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}};
        for (auto& dir : directions) {
            int nr = dir[0], nc = dir[1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                && board[nr][nc] != '#' && node->children.find(board[nr][nc]) != node->children.end()) {
                dfs(nr, nc, node, word + board[nr][nc]);
            }
        }

        // now backtrack if we don't ans by adding the char at (r,c)
        board[r][c] = temp;
    }
};

"""