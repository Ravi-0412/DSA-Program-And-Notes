# method 1:
"""
using Two tries

1. We maintain two separate Tries. One stores words normally for prefix lookups, 
and the other stores words in reverse for suffix lookups.
2. Tracking Indices: Every character node in the Trie acts as a "checkpoint.
" It doesn't just point to the next letter; it also keeps a list (a set) of every word index that has passed through it.
3. The Search Flow:
i)  To find a prefix, we traverse the prefixTrie. The node we land on contains all indices of words starting with that prefix.
ii) To find a suffix, we reverse the suffix string (e.g., "le" becomes "el") and traverse the suffixTrie. 
The node we land on contains all indices of words ending with that suffix.
4. Intersection: The answer must be in both sets. We intersect them and pick the largest number.

Time (Constructor): O(N * L). We process $N$ words of length L twice.
Time (Function f): O(P + S + N)$ We spend O(P) and O(S) traversing the Tries.
The set intersection & can take up to O(N) in the worst case (if all words share the same prefix and suffix).

Space: O(N * L * N) worst case. While the Trie nodes are O(N * L), 
storing the set of indices at every node can significantly increase memory usage.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the indices of all words that share this path
        self.indices = set()

class WordFilter:
    def __init__(self, words: List[str]):
        self.prefixTrie = TrieNode()
        self.suffixTrie = TrieNode()
        
        for index, word in enumerate(words):
            # Normal word for prefix matching
            self.insert(self.prefixTrie, word, index)
            # Reversed word for suffix matching
            self.insert(self.suffixTrie, word[::-1], index)

    def insert(self, root, word, index):
        curr = root
        curr.indices.add(index)
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.indices.add(index)

    def search(self, root, query):
        curr = root
        for char in query:
            if char not in curr.children:
                return set()
            curr = curr.children[char]
        return curr.indices

    def f(self, pref: str, suff: str) -> int:
        # Step 1: Find all indices matching the prefix
        prefix_indices = self.search(self.prefixTrie, pref)
        
        # Step 2: Find all indices matching the suffix (by searching reversed)
        suffix_indices = self.search(self.suffixTrie, suff[::-1])
        
        # Step 3: Find common indices between the two sets
        common = prefix_indices & suffix_indices
        
        # Step 4: Return the largest index as per requirements
        if not common:
            return -1
        return max(common)

  # Method 2:
  """
  using Single Trie

Instead of two Tries, we use one. For a word like "apple", we insert several combinations into the Trie
so that any suffix/prefix pair can be found in a single top-down traversal:

#apple

e#apple

le#apple

ple#apple

... and so on.

Time: 
Search Time O(pref + suff): There is no set intersection, no loops, and no max(). 
It’s a direct walk down the tree.
Space : O(N * L^2): It uses more memory than the two-trie approach, 
but within the constraints (L <= 7), this is perfectly acceptable.
  """


class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores only the latest (largest) index seen at this path
        self.max_index = -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        # We iterate through words. Later indices will overwrite earlier ones.
        for index, word in enumerate(words):
            self.insert_all_suffix_combinations(word, index)

    def insert_all_suffix_combinations(self, word: str, index: int):
        # We create the "google trick" string: suffix + # + prefix
        # Example: for "apple", one combo is "le#apple"
        combined = word + "#" + word
        n = len(word)
        
        # We must start a new insertion path for every possible suffix
        for i in range(n + 1):
            curr = self.root
            # Slicing from i gives us: "apple#apple", "pple#apple", "ple#apple"...
            suffix_plus_prefix = combined[i:]
            
            for char in suffix_plus_prefix:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # Overwrite with the current index (guaranteed to be the largest so far)
                curr.max_index = index

    def f(self, pref: str, suff: str) -> int:
        # To find a word with prefix 'pref' and suffix 'suff',
        # we search for the specific path: 'suff' + '#' + 'pref'
        search_query = suff + "#" + pref
        curr = self.root
        
        for char in search_query:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
            
        # If we reach the end of the query, the max_index at this node
        # represents the largest index word that matches BOTH constraints.
        return curr.max_index
