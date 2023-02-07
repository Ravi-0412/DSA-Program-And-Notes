# method  1:
# time: O(K*N), k: length of shortest string, N: no of words

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest= min(strs, key= len)   # will give the smallest word from the given words according to the length
        # now check till where all words matches to this shortest word.
        # where it doesn't matches then simply return till that index.
        for i in range(len(shortest)):
            for w in strs:
                if w[i]!= shortest[i]:
                    return shortest[:i]
        # means shortest is our required ans
        return shortest

# same logic. we can start with even first char and do the same.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans= ""
        for i in range(len(strs[0])):
            for w in strs:
                if i== len(w) or strs[0][i]!= w[i]:
                    return ans


# method 2:
# time: O(n* logn)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n= len(strs)
        if n== 1:
            return strs[0]
        strs.sort()   # sort the array
        # now just find the prefix of first and last word, that will be the ans
        check_till= min(len(strs[0]), len(strs[n-1]))
        i= 0
        while i < check_till and strs[0][i]== strs[n-1][i]:
            i+= 1
        ans= strs[0][: i]
        return ans


# method 3: using TRie
class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class Trie:
    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
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
    
    def LongestPrefix(self, word, ans):
        cur= self.root
        for c in word:
            if len(cur.children) > 1:
                return ans
            ans+= c
            cur= cur.children[c]
        return ans



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie= Trie()
        for s in strs:
            trie.insert(s)
        # now take any word and keep adding the char of this word to ans till you don't find more than one children.
        # and when you find more than one children at any node , then simply return the ans.
        shortest= min(strs, key= len)
        ans= ""
        ans= trie.LongestPrefix(shortest, ans)
        return ans