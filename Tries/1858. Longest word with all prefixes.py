# Time: O(n* l)  , n= no of words and l= length of each word.

class TrieNode:
    def __init__(self):
        self.children= {}  # will point to children. and can be max of 26('a' to 'z').   (just like 'next' in linklist)
        self.isEndOfWord= False   # will mark True if that node is the last node of the word otherwise False for each node.

class Trie:

    def __init__(self):
        self.root= TrieNode()   # for every word, we will always start checking from root.
    
    def LongestWord(self, words):
        # First insert all the words in the Trie
        for word in words:
            self.insert(word)

        # now traverse each word and find the ans if all the prefix of word exists.
        longest= ""
        for word in words:
            if self.ifAllPrefixExists(word):
                if len(word) > len(longest):
                    longest= word
                elif len(word)== len(longest) and longest > word :  # when length is same, we have to take the word alphabetically small.
                    longest= word
        return None if longest== "" else longest

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

    def ifAllPrefixExists(self, word):
        cur= self.root
        for c in word:
            cur= cur.children[c]
            if cur.isEndOfWord== False:  
                return False
        return True

T= Trie()
# words= ["n", "ni", "nin", "ninj", "ninja", "ninga"]
# words= ["n", "ni", "nin", "ninj", "ninja", "ninga", "ninjas"]
words= ["np", "nhi", "nikn", "ninj"]
# words= []
print("longest word with all prefixes is: ", T.LongestWord(words))



# Note: Try to do by find the ans by using dfs after inserting..Link in the sheet.

