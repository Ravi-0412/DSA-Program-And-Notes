# same way as we search but if there is '.' then we have to check all the possibility at that node.
# that case we have chheck using dfs(backtrcaking).
class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()
        
    def addWord(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        # now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord= True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    
    def dfs(self, word, ind, root):
        cur= root
        for i in range(ind, len(word)):
            c= word[i]
            if c== '.':
                for child in cur.children.values():
                    if self.dfs(word, i+1, child):   # if any of one return True then no need to check other path.
                        return True
                # if neither of path return True then return False
                return False
            else:  # means there is letter.
                if c not in cur.children:
                    return False
                cur= cur.children[c]
        # now we are at last children node of the word
        return cur.isEndOfWord


# other way 
# i thought like this.
class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()
        
    def addWord(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
        # now we have inserted all the char of 'word', so make 'cur.isEndOfWord= True'. will denote the 'word' end at this node.
        cur.isEndOfWord= True
    
    def search(self, word: str) -> bool:

        def solve(word, root):
            # if not word:  # no need of this
            #     return root.isEndOfWord
            cur= root
            for i in range(len(word)):
                c= word[i]
                if c!= '.':
                    if c not in cur.children:
                        return False
                    cur= cur.children[c]
                else:
                    for num in range(97, 123):
                        ch= chr(num)
                        if ch in cur.children:
                            if solve(word[i+ 1: ], cur.children[ch]):
                                return True
                    return False  # no children is present 
            return cur.isEndOfWord

        return solve(word, self.root)