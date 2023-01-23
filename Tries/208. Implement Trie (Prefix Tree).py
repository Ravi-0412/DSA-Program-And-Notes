# Time complexity of all is O(n).

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

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return False
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur.isEndOfWord   # this is made 'True' to the child node of last char of the word.

    def startsWith(self, prefix: str) -> bool:
        cur= self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur= cur.children[c]
        # it means all char of prefix is present. so simply return True
        return True


# Note: we can use trie where we are sure that every ele or every word will be made only from a fixed thing like number or letter.
# so that there is no need to create or check from scratch for every ele.

# 1) every word can be made only from letters 'a-z' i.e every ele in word will start from 'a-z' only. will have characters only from 'a-z'.
# 2) Every number when treated as Binary will have bit only '0' and '1'.
# 3) used in creating / searching word in dictionary
# 4) used to predict the possible word based on few typed words. e.g: Google Search Engine.
# 5) used to fine the word 'starting with', 'Ending With' etc with a given substring.
