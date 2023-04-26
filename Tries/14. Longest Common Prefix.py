# method  1:
# time: O(K*N), k: length of shortest string, N: no of words

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest= min(strs, key= len)   # will give the smallest word from the given words according to the length
                                        # time: O(n)
        # now check till where all words matches to this shortest word.
        # where it doesn't matches then simply return till that index.
        for i in range(len(shortest)):
            for w in strs:
                if w[i]!= shortest[i]:
                    return shortest[:i]
        # means shortest is our required ans
        return shortest

# same logic. we can start with even first char and do the same.
# we can do the same for every word like above because that prefix should be present in every word.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans= ""
        for i in range(len(strs[0])):
            for w in strs:
                if i== len(w) or strs[0][i]!= w[i]:
                    return ans
            ans+= strs[0][i]
        return ans


# method 2:
# time: O(n* logn)

# sort the array
# And now just find the prefix of first and last word, that will be the ans.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n= len(strs)
        if n== 1:
            return strs[0]
        strs.sort()   
        check_till= min(len(strs[0]), len(strs[n-1]))
        i= 0
        while i < check_till and strs[0][i]== strs[n-1][i]:
            i+= 1
        ans= strs[0][: i]
        return ans


# method 3: using TRie
# insert all words in Trie

# now take smallest word in len and keep adding the char of this word to ans till you don't find more than one children.
# Because if there is more than one children then it means word start differentiating from that node (means char are differing from that index).
# Since till common prefix there will be only char in each children.

# so when you find more than one children at any node , then simply return the ans.

# note: if you take any word say strs[0] then it will give incorrect ans because we go ahead with the refernec of pointer.
# e.g: ["ab", "a"] # will give => "ab" instead of "a".

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
        shortest= min(strs, key= len)
        ans= ""
        ans= trie.LongestPrefix(shortest, ans)
        return ans