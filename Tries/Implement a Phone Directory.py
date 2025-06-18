# Method 1: 

# for every prefix in 'search_contact(qList)' , we have to return all contacts starting from that 'prefix'. 

class TrieNode:
    def __init__(self):
        self.children = {}         # Dictionary to hold child nodes for each character
        self.isEndOfWord = False   # True if the node marks the end of a contact

class Trie:
    def __init__(self):
        self.root = TrieNode()     # Root node of the Trie

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # If character is not present, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  # Move to the next node
        cur.isEndOfWord = True     # Mark the end of the word

class Solution:
    def displayContacts(self, n, contact, s):
        ans = []
        trie = Trie()

        # Insert all contacts into the Trie
        for word in set(contact):  # Use set to avoid duplicates
            trie.insert(word)

        prefix = ""
        pre = trie.root

        # For every character in query string 's'
        for c in s:
            # If prefix is not present in Trie, break and fill remaining with "0"
            if c not in pre.children:
                break
            prefix += c
            temp = []
            self.getSuggestions(pre.children[c], temp, prefix)
            ans.append(temp)
            pre = pre.children[c]

        # If no match found at any point, fill remaining results with ["0"]
        while len(ans) < len(s):
            ans.append(["0"])

        return ans

    def getSuggestions(self, cur, temp, prefix):
        # If a complete word ends at this node, add it to result list
        if cur.isEndOfWord:
            temp.append(prefix)
             # return            # because we can get the more words follwing the same path like tree.

        # Recursively search for all children nodes in lexicographical order
        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if char in cur.children:
                self.getSuggestions(cur.children[char], temp, prefix + char)


