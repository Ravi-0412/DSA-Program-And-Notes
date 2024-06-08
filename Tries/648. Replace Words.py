# method 1: 

# Q: just we have to replace every word in sentense with its "smallest prefixes present in the dictionary".

# method 1: using hashmap
# Exactly similar to what i did in "677. Map Sum Pairs".
# Time: o(N^3)
# will try myself using hashmap

# logic: since we are updating every time "sentence[i]" and replacing it with string it startswith.
# so at last we will get the smallest "starting prefix only"
class Solution(object):
    def replaceWords(self, dict, sentence):
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            for j in dict:
                if sentence[i].startswith(j):
                    sentence[i] = j     # changing everytime and later checking with updated one.
        return " ".join(sentence)


# logic: just put all words of dictionary into Trie 

# then traverse each word in sentence and search for its smallest prefix in dictionary(Trie)
# i.e first node where we will get 'node.isEndOfWord= True'.

# if doesn't have any prefix then return "" at that time itself.

class TrieNode:
    def __init__(self):
        self.children= {}  
        self.isEndOfWord= False   

class Trie:

    def __init__(self):
        self.root= TrieNode()   
        
    def insert(self, word: str) -> None:
        cur= self.root
        for c in word:
            if c not in cur.children:  # no prefix of word is present in dictionary
                cur.children[c]= TrieNode()
            cur= cur.children[c]
        cur.isEndOfWord= True

    def search(self, word: str) -> bool:   # will giev the smallest prefix of word which is presnet in the dictionary i.e 'isEndOfword= True'.
        prefix= ""
        cur= self.root
        for c in word:
            if c not in cur.children:
                return ""
            cur= cur.children[c]
            prefix+= c
            if cur.isEndOfWord:  # check if this prefix is present.
                return prefix  

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie= Trie()
        for word in dictionary:
            trie.insert(word)
        sentence= sentence.split()
        for i in range(len(sentence)):
            prefix= trie.search(sentence[i])
            if prefix:  # means if any prefix of 'word' is present in the dictionary.
                sentence[i]= prefix
        return " ".join(sentence)

# my mistake in accessing the word of dictionary.
# that why convert the sentence into list.


# for word in sentence:   # this will give letter not word. (what the fucking mistake i was making).
    for i in range(len(sentence)):  # same here
        word= sentence[i]
        prefix= trie.search(word)

        