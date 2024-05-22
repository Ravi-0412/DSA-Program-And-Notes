
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



# Java version for 1st method:
"""

public class Solution {
    public class TrieNode{
        public boolean isWord = false;
        public TrieNode[] child = new TrieNode[26];
        public TrieNode(){
            
        }
    }
    
    TrieNode root = new TrieNode();
    boolean[][] flag;   // for marking visited
    public List<String> findWords(char[][] board, String[] words) {
        Set<String> result = new HashSet<>();
        flag = new boolean[board.length][board[0].length];
        
        addToTrie(words);
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(root.child[board[i][j] - 'a'] != null){
                    search(board, i, j, root, "", result);
                }
            }
        }
        return new ArrayList<>(result);
        // return new LinkedList<>(result);
    }
    
    private void addToTrie(String[] words){
        for(String word: words){
            TrieNode node = root;
            for(int i = 0; i < word.length(); i++){
                char ch = word.charAt(i);
                if(node.child[ch - 'a'] == null){
                    node.child[ch - 'a'] = new TrieNode();
                }
                node = node.child[ch - 'a'];
            }
            node.isWord = true;
        }
    }
    
    private void search(char[][] board, int i, int j, TrieNode node, String word, Set<String> result){
        if(i >= board.length || i < 0 || j >= board[i].length || j < 0 || flag[i][j] || node.child[board[i][j] - 'a'] == null){
            return;
        }
        
        word += board[i][j] ;
        flag[i][j] = true;
        node = node.child[board[i][j] - 'a'];
        if(node.isWord){
            result.add(word);
        }
        
        search(board, i-1, j, node, word, result);
        search(board, i+1, j, node, word, result);
        search(board, i, j-1, node, word, result);
        search(board, i, j+1, node, word, result);
        
        flag[i][j] = false;
    }
}

"""