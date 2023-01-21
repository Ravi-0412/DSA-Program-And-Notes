# method 1: Brute Force
# logic: Take all substrings that can be generated from fixing an index. (same logic as GFG solution)
# Time: O(n^3)
# space: O(n^3). There will be n^2 substrings and average length will be 'n/2'.


# method 2: using Trie
# just insert each substring possible from each index.
# and count only if that substring is not present in the children for distinct one.

# time: O(n^2) . 
# space: can't be determined exactly but will be very less than O(n^3) in nature.

class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        
def countDistinctSubstrings(s):
    root= TrieNode()
    count= 1    # we have to include empty string also
    # just insert the substring starting from each char.
    for i in range(len(s)):
        cur= root
        for j in range(i, len(s)):
            if s[j] not in cur.children:   # only need to insert s[j] since we are doing by Trie.
                cur.children[s[j]]= TrieNode()
                count+= 1
            cur= cur.children[s[j]]
    return count
