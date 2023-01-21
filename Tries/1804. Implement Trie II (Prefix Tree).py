# little bit modified the functions to get the ans easily.
# just same logic only

# note: for finding the no of words starting with any 'word', just 'count the no of len(children) of last node of word + no of occurence of that word itself'.

# submitted on codingninja.
class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.word_count= 0     # will tell the frequency of word. (nose at which we were marking 'isEndOfWord= True', there we will increase this count)
        self.prefix_count= 0   # will tell no of word staring with a given prefix. after every node you are inserting increase this count.

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
            # increase the prefix count of this node.
            cur.prefix_count+= 1
        # now increase the word_count for this node.
        cur.word_count+= 1

    def countWordsEqualTo(self, word):
        node= self.search(word)
        return 0 if node== None else node.word_count
    
    def countWordsStartingWith(self, prefix: str) -> bool:
        node= self.search(prefix)
        return 0 if node== None else node.prefix_count
    
    # for erasing the word, just decr the count of each prefix and count of word itself.
    def erase(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
            cur.prefix_count-= 1
        cur.word_count-= 1

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return None
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur

    