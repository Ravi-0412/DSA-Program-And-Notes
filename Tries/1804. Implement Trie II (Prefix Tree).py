# little bit modified the functions to get the ans easily.
# just same logic only

# Note: we are updating 'word_count' and 'prefix_count' after each node like 'isEndOfWord'.

# submitted on codingninja.
class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.word_count= 0     # will tell the frequency of word. (node at which we were marking 'isEndOfWord= True', there we will increase this count)
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
            cur= cur.children[c]
            # After inserting node increase its prefix_count
            cur.prefix_count+= 1
        # now increase the word_count for this node.
        # cur.prefix_count+= 1  # we have already updated prefix_count for this node loop itself.
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
        # cur.prefix_count-= 1    # we have already updated prefix_count for this node loop itself.
        cur.word_count-= 1

    # A node has more than more ans(wordCount or prefixCount) so just return 'node' itself because we don't know what ans we will have to return from this node.

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return None
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur


# another way
class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
        self.prefixes= [0, 0]  # 1st : will tell no of word ending at that node and if =0 means no word end at that node.and
                               # 2nd:  will tell no of word which has this prefix and if =0 means no prefix at that node.
                # just took prefixes instead of 'isEndOfWord'                      
class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
        
    def insert(self, word):
        cur= self.root
        for c in word:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            cur= cur.children[c]
            # After inserting node increase its prefix_count
            cur.prefixes[1]+= 1
        # now increase the word_count for this node.
        cur.prefixes[0]+= 1

    def countWordsEqualTo(self, word):
        node= self.search(word)
        return 0 if node== None else node.prefixes[0]
    
    def countWordsStartingWith(self, prefix: str) -> bool:
        node= self.search(prefix)
        return 0 if node== None else node.prefixes[1]
    
    # for erasing the word, just decr the count of each prefix and count of word itself.
    def erase(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
            cur.prefixes[1]-= 1
        cur.prefixes[0]-= 1

    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return None
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return cur
    

# Note: whenever you have to remove any word apply the prefix_count with isEndofWord(or word_count).
# while adding incr the count of both and while removing decr the count.