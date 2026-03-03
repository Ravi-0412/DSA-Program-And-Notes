"""
Rule 1: Characters must match in order.
Rule 2: If the word's block is smaller than the target $s$, you can only stretch it if the target s block size is 3 or more.
Rule 3: If the word's block is already larger than the target s, it's impossible (you can't "shrink").
Time = O(n), space: O(1)
"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i, j = 0, 0
            n, m = len(s), len(word)
            
            while i < n and j < m:
                if s[i] != word[j]: return False
                
                # Get block size for s
                char = s[i]
                count_s = 0
                while i < n and s[i] == char:
                    i += 1
                    count_s += 1
                
                # Get block size for word
                count_w = 0
                while j < m and word[j] == char:
                    j += 1
                    count_w += 1
                
                # Logic Check:
                # 1. Word block can't be bigger than target
                # 2. If different, target must be >= 3
                if count_w > count_s: return False
                if count_w < count_s and count_s < 3: return False
                
            return i == n and j == m

        return sum(1 for word in words if is_stretchy(word))

# Follow ups:
"""
1. How will you reduce the number of operations inside the loop significantly ?
Nas: 
1. Optimization: Pre-counting s
Logic & Thought Process
In the basic two-pointer version, for every word in the input list, we re-scan s. If words has 1,000 strings, we scan s 1,000 times.
The Fix: Compress s into a list of "Run-Length Encoded" (RLE) blocks first.

Target s: "heeellooo" → [('h', 1), ('e', 3), ('l', 2), ('o', 3)]

Now, for each word, we just need to check if its blocks can "stretch" to match these pre-calculated targets.

Time = space = O(n)
"""

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # Pre-process s once to optimize comparison time
        s_blocks = self.get_rle(s)
        count = 0
        
        for word in words:
            w_blocks = self.get_rle(word)
            if self.is_stretchy(s_blocks, w_blocks):
                count += 1
        return count

    def get_rle(self, string: str):
        # Helper to compress string into (char, frequency) blocks
        if not string: return []
        res = []
        char, freq = string[0], 0
        for c in string:
            if c == char:
                freq += 1
            else:
                res.append((char, freq))
                char, freq = c, 1
        res.append((char, freq))
        return res

    def is_stretchy(self, s_blocks, w_blocks) -> bool:
        # Check if number of distinct character groups matches
        if len(s_blocks) != len(w_blocks):
            return False
            
        for (s_char, s_count), (w_char, w_count) in zip(s_blocks, w_blocks):
            # Combined Failure Condition:
            # 1. Chars don't match OR 
            # 2. Word has more chars than s OR 
            # 3. s has more chars than word but s group size is < 3
            if s_char != w_char or w_count > s_count or (w_count < s_count and s_count < 3):
                return False
        
        return True

"""
Follow ups 2. Stream Pivot: "Can you handle a stream?"
Q clarification: 
The Scenario: You don't have s as a fixed string. Instead, characters are arriving one by one from a network or a sensor. 
You have a dictionary of words. At any moment, you need to be able to say: "Whether words in my dictionary could be the 'stretchy' source of the stream I just saw?"
Just True / False .
"""

class TrieNode:
    def __init__(self):
        # Maps char -> list of tuples: [(required_count, next_node), ...]
        self.children = {} 
        self.is_word = False

class StretchyStreamer:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self._insert(word)

    def _get_rle(self, string):
        # Helper: standard RLE compression
        if not string: return []
        res = []
        char, freq = string[0], 0
        for c in string:
            if c == char: freq += 1
            else:
                res.append((char, freq))
                char, freq = c, 1
        res.append((char, freq))
        return res

    def _insert(self, word):
        # Insert word into Trie based on its RLE structure
        rle = self._get_rle(word)
        node = self.root
        for char, count in rle:
            if char not in node.children:
                node.children[char] = []
            
            # Check if this count/branch already exists to save space
            found_node = None
            for req_count, next_node in node.children[char]:
                if req_count == count:
                    found_node = next_node
                    break
            
            if not found_node:
                found_node = TrieNode()
                node.children[char].append((count, found_node))
            node = found_node
        node.is_word = True

    def check_stream(self, stream_str):
        # 1. Compress the incoming stream
        stream_rle = self._get_rle(stream_str)
        
        # 2. Use DFS to find if any Trie path matches the stretchy logic
        def dfs(rle_idx, node):
            # If we've processed all stream blocks, check if we're at a word end
            if rle_idx == len(stream_rle):
                return node.is_word
            
            s_char, s_count = stream_rle[rle_idx]
            if s_char not in node.children:
                return False
            
            # Try all possible required_counts for this character
            for w_count, next_node in node.children[s_char]:
                # Apply the Expressive Words logic
                can_stretch = (w_count == s_count) or (s_count > w_count and s_count >= 3)
                
                if can_stretch:
                    if dfs(rle_idx + 1, next_node):
                        return True
            return False

        return dfs(0, self.root)

# Example Usage:
# streamer = StretchyStreamer(["hello", "hi", "helo"])
# print(streamer.check_stream("heeellooo")) -> True
