"""
Question: 
Given an array of unique strings words, return all the word squares you can build from words. 
The same word from words can be used multiple times. You can return the answer in any order.
A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).
For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads 
the same both horizontally and vertically.

Example 1:

Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:

Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 4
    All words[i] have the same length.
    words[i] consists of only lowercase English letters.
    All words[i] are unique.

"""


# Basic 
"""
A "Word Square" means that if you have $k$ words, the $k$-th row must be identical to the k-th column.
(Transpose)

When you are trying to pick the next word (row $i$), you don't just pick any word. You are restricted by the words you already picked. 
Specifically, the prefix of the next word must match the characters already placed in that column.
Example: If your first word is BALL: 
i) Row 0: B A L L
ii) Column 0 must also be B A L L. 
iii) This means Row 1 must start with A, Row 2 must start with L, and Row 3 must start with L.
"""

# Method 1 :
"""
The Brute Force Logic :
Try every possible combination of words to see if they form a valid square. 
Since all words have length L, a word square must have L rows. We have N words to choose from.
i) Pick any word for Row 0.
ii) Pick any word for Row 1
iii) .... continue until you have L words.
iv) Check: Is this a valid Word Square? (Does Row $k$ == Column k for all k?)

Time : (O(N^L))
"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words)
        L = len(words[0])
        results = []
        
        def is_valid(square):
            # Check if Row k == Column k
            # Transpose , just same logic as: Valid word square
            for r in range(L):
                for c in range(L):
                    if square[r][c] != square[c][r]:
                        return False
            return True

        def backtrack(curr_square):
            # Base Case: We have picked L words
            if len(curr_square) == L:
                if is_valid(curr_square):
                    results.append(list(curr_square))
                return
            
            # Try every single word in the list for the next row
            for word in words:
                curr_square.append(word)
                backtrack(curr_square)
                curr_square.pop() # Backtrack

        backtrack([])
        return results

# Method 2:
"""
Optimising a bit.

Instead of picking a word and checking validity at the end, we should check validity at every step.
If we have picked 2 words:
BALL
AREA
The next word (Row 2) must start with the characters found at index 2 of the previous words.
Word 0, Index 2: L
Word 1, Index 2: E
Therefore, the 3rd word must start with LE.

Time : (O(N^L)) but will be faster
"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        L = len(words[0])
        results = []

        def backtrack(step, curr_square):
            if step == L:
                results.append(list(curr_square))
                return
            
            # Calculate the prefix needed for the next row
            # If step = 2, we need char at index 2 from word 0 and word 1
            prefix = "".join([word[step] for word in curr_square])
            
            # Optimization: Only try words that start with 'prefix'
            for word in words:
                if word.startswith(prefix):
                    curr_square.append(word)
                    backtrack(step + 1, curr_square)
                    curr_square.pop()

        for word in words:
            backtrack(1, [word])
        return results

# Method 3:
"""
The goal here is to replace the slow for word in words: if word.startswith(prefix) (which is O(N)) with a Trie lookup (which is O(L)).
To get to know from which all words , a prefix has been generated , we will store 'list of such words'
say 'word_with_prefix' also for each node which is a game changer and reduce complexity from O(N) to O(L).

Time$O(N * 26^L)
In the worst case, we explore many branches. However, the symmetry constraint prunes the search space so aggressively
that the actual time is much closer to $O(N * L^2). 
Space : O(N * L), We store every word of length L in the Trie or Hash Map. 
For the Trie, this is the number of nodes; for the Hash Map, it's the number of prefix keys.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores all words that share the prefix path leading to this node
        self.words_with_prefix = []

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.L = len(words[0])
        self.root = TrieNode()
        
        # Build Trie: O(N * L)
        for word in words:
            node = self.root
            node.words_with_prefix.append(word) # Root handles empty prefix
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.words_with_prefix.append(word)
        
        results = []
        # Try every word as the first row (Row 0)
        for word in words:
            self.backtrack([word], results)
        return results

    def backtrack(self, curr_square, results):
        # BASE CASE: We have filled L rows, meaning we have a L x L square
        if len(curr_square) == self.L:
            results.append(list(curr_square))
            return
        
        # SYMMETRY LOGIC:
        # If we are filling Row 1, the prefix must be the char at index 1 of Row 0.
        # If we are filling Row 2, the prefix must be (Row 0 [index 2] + Row 1 [index 2]).
        # This "vertical slice" ensures that Row K will match Column K.
        row_idx = len(curr_square)
        prefix = "".join([word[row_idx] for word in curr_square])
        
        # Retrieve all candidate words that start with the required prefix
        candidates = self.get_words_by_prefix(prefix)
        
        for candidate in candidates:
            curr_square.append(candidate) # Choose
            self.backtrack(curr_square, results) # Explore
            curr_square.pop() # Un-choose (Backtrack)

    def get_words_by_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words_with_prefix

# Method 4: 
"""
Using Hashmap

Why use Hash Map over Trie?
Pros: Much faster to code (no extra class needed); slightly faster lookups in Python due to optimized dictionary hashing.

Cons: Uses slightly more memory because string prefixes are stored as actual keys rather than paths in a tree.

Time Complexity ;
Preprocessing: O(N * L^2). 
We iterate through $N$ words. For each word, we create L prefixes. 
In Python, string slicing word[:i] takes O(L) time, leading to L *L per word.
Backtracking : O(N * 26^L). 
This is the theoretical upper bound (similar to the Trie). 
However, because we only pick words that perfectly fit the symmetry, the actual time is significantly lower. 

Space : O(N * L*L), We store N words. For each word, we store L prefixes as keys in the map. 
Each prefix can be up to length L. Thus, N \times L * L.
"""

from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        L = len(words[0])
        # Key: Prefix, Value: List of words starting with that prefix
        prefix_map = defaultdict(list)
        
        # Pre-processing: O(N * L)
        for word in words:
            # Add every possible prefix of the word to the map
            # e.g., "BALL" -> "", "B", "BA", "BAL", "BALL"
            for i in range(L + 1):
                prefix = word[:i]
                prefix_map[prefix].append(word)
        
        results = []

        def backtrack(curr_square):
            # Base Case: Square is full
            if len(curr_square) == L:
                results.append(list(curr_square))
                return
            
            # Identify the required prefix for the current row
            # based on the symmetry of the square (Column index matches Row index)
            idx = len(curr_square)
            prefix = "".join([word[idx] for word in curr_square])
            
            # If no words in our vocabulary start with this prefix, prune this branch
            if prefix not in prefix_map:
                return
            
            # Try all valid words for this row
            for candidate in prefix_map[prefix]:
                curr_square.append(candidate)
                backtrack(curr_square)
                curr_square.pop()

        # Start the recursion with an empty square
        backtrack([])
        return results
