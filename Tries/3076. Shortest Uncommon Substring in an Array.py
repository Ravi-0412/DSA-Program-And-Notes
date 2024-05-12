# Brute force:

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = []
        for word in range(len(arr)):
            resSub = "{zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz" # ascii value of '{' is larger than 'z' that's why used it. 
                    # Also to match the 'shortest length' criterion, added multiple z around 20 times. you can add anything since it will always be lexicographically greater.
            for i in range(len(arr[word])):
                for j in range(i, len(arr[word])):
                    sub = arr[word][i:j+1]  # Checking every sub string (simple brute force)
                    flag = 1  # to check if the substring appeared in any other string of arr
                    for wd in range(len(arr)):
                        if wd == word:  # skip the word from which sub is selected
                            continue
                        if sub in arr[wd]:  # hence invalid substring
                            flag = 0
                            break
                    
                    if (len(sub) <= len(resSub)) and flag == 1: # to match the shortest length criteria
                        if (sub < resSub or len(sub) < len(resSub)): # to match the lexicography
                            resSub = sub
 
                
            if resSub == "{zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz":
                resSub = ""
                
            res.append(resSub)
        return res


# Optimised one:
# using Trie

# Logic: Store all substring of every word in trie 
# and to chekc whether that substring is present in how many word we will insert each substring with some number
# say index of word.

# Now for ans traverse each substring of a word and for each substring check in how many word that substring is present.
# If present in same word only then store that substring into ans and after that return the smallest one.

# Time: O(m * n*n) = O(100*20*20), m = no of string and n = length of each string

class TrieNode:
    def __init__(self):
        self.children = {}
        self.noSubFromDifferentWord = set()   # no of substring from different words
                                              # Will tell in how many words this substring is present.

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, num):
        n = len(word)
        for i in range(n):
            cur = self.root
            for j in word[i : ] :
                if j not in cur.children:
                    cur.children[j] = TrieNode()
                cur = cur.children[j]
                cur.noSubFromDifferentWord.add(num)
    
    def find(self, word):
        n = len(word)
        ans = []
        for i in range(n):
            cur = self.root
            cur_subs = ""
            for j in word[i : ]:
                cur_subs += j
                cur = cur.children[j]
                if len(cur.noSubFromDifferentWord) == 1:
                    ans.append(cur_subs)
                    break
        # sort based on length and in case of equal sort according to smallest lexographical order
        return sorted(ans, key = lambda x : (len(x), x))[0] if ans else ""

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()

        for i, word in enumerate(arr):
            trie.insert(word, i)
        
        ans = []
        for word in arr:
            ans.append(trie.find(word))
        return ans



        