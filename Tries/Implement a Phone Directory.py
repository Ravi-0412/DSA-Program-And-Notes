# for every prefix in 'search_contact(qList)' , we have to return all contacts starting from that 'prefix'. 

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

def phoneDirectory(arr,qList):
    ans= []
    trie= Trie()
    for word in arr:
        trie.insert(word)
        
    prefix= ""
    pre= trie.root
        
    for c in qList:
        if c not in pre.children:
            break
        prefix+= c
        temp= []   # will store the words which have prefix= prefix.
        next= pre.children[c] # we will start checking from here only if next is endOfWord or not.
        getSuggestions(pre.children[c], temp, prefix)
        ans.append(temp)
        temp = []
        pre= next    # to chekc for next prefix matching words

    return ans


def getSuggestions(cur, temp, prefix):
        if cur.isEndOfWord:
            temp.append(prefix)
            # return            # because we can get the more words follwing the same path like tree.
        
        for i in range(ord('a'), ord('z') + 1):   # we have to add char of every node and only way we can do like this.
            char= chr(i)
            if char in cur.children:
                next= cur.children[char]
                getSuggestions(next, temp, prefix + char)


# we can write the above code like this

def phoneDirectory(arr,qList):
    ans= []
    trie= Trie()
    for word in arr:
        trie.insert(word)
        
    prefix= ""
    pre= trie.root
        
    for c in qList:
        if c not in pre.children:
            break
        prefix+= c
        temp= []
        getSuggestions(pre.children[c], temp, prefix)
        ans.append(temp)
        temp = []
        pre= pre.children[c]

    return ans
