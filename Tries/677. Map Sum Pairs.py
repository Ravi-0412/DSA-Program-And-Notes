# method 1: Brute force.
# put all key in hashmap and keep updating with latest value.

# for sum:
# check all key present in hashamsp if they startswith "prefix" .

# time complexity:  O(K^2) for each 'sum' function.
class MapSum:
    def __init__(self):
        self.hashmap= collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key]= val

    def sum(self, prefix: str) -> int:
        ans= 0
        for s in self.hashmap:
            if s.startswith(prefix):
                ans+= self.hashmap[s]
        return ans


# method 2: using Trie

# logic: we have to count the val of every word which has prefix as given "prefix".
# so for every node we have to store the 'key' and keep on adding for another key at same node.

# for insert:
# 1) first we will check whether that key is already present or not.
# 1.a) if present then at every node where key char is present , we will have to update with new val.
# for updating we will need the preVal. for getting preVal we are storing the 'val' with isEndOfWord.

# After getting pre value we will update prefix_sum like:  cur.prefix_sum= cur.prefix_sum - preVal + val .

# 2) if not present then simply insert and each node keep on adding this 'val' to the node.prefixSum.

# Time:
# insert: O(K), where K <= 50 is length of key string.
# sum: O(P), where P <= 50 is length of prefix string.
# Space: O(T), where T is the total of nodes after inserting all key string, T <= total characters of key strings.

class TrieNode:
    def __init__(self):
        self.children= {}
        self.isEndOfWord= [False, 0]  # will tell 'isEndOfWord' then what is the value of that key(word).
        self.prefix_sum= 0

class MapSum:

    def __init__(self):
        self.root= TrieNode()
    
    def search(self, word: str) -> bool:
        cur= self.root
        for c in word:
            if c not in cur.children:
                return False, 0
            cur= cur.children[c]
        return cur.isEndOfWord
    
    def update(self, key, val, preVal):
        cur= self.root
        for c in key:
            cur= cur.children[c]
            # update the prefix sum.
            cur.prefix_sum= cur.prefix_sum - preVal + val
        # cur.isEndOfWord[0]= True # no need already marked as True since it is present already.
        cur.isEndOfWord[1]= val

    def insert(self, key: str, val: int) -> None:
        isPresent, preVal= self.search(key)
        if isPresent: # then update everywhere with cur 'val'.
            self.update(key, val, preVal)
        else:  # means this key is not present in Trie then simply insert 
            cur= self.root
            for c in key:
                if c not in cur.children:
                    # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                    cur.children[c]= TrieNode()
                # after inserting and if present already ,move cur to next child in both cases.
                cur= cur.children[c]
                # increase the prefix sum.
                cur.prefix_sum+= val
            # now increase the word_count for this node.
            cur.isEndOfWord[0]= True
            cur.isEndOfWord[1]= val

    def sum(self, prefix: str) -> int:
        cur= self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur= cur.children[c]
        return cur.prefix_sum


# method 3: Easier one
# trie + Hashmap(for stroing the pre val of key).
# we will update the val of prefix_sum like cur.prefix_sum+= valDiff where valDiff= val- self.hashmap[key]   # (if not present then self.hashmap[key]= 0).

# Doing the same thing.

class TrieNode:
    def __init__(self):
        self.children= {}
        self.prefix_sum= 0

class MapSum:

    def __init__(self):
        self.root= TrieNode()
        self.hashmap= collections.defaultdict(int)  # [key: val] , will store the last val of 'key'.
    
    def insert(self, key: str, val: int) -> None:
        valDiff= val- self.hashmap[key]   # (if not present then self.hashmap[key]= 0)
        cur= self.root
        for c in key:
            if c not in cur.children:
                # insert 'c' into chilren and make 'c' point to a TrieNode and move curr to next child(just added one)
                cur.children[c]= TrieNode()
            # after inserting and if present already ,move cur to next child in both cases.
            cur= cur.children[c]
            # update the prefix sum.
            cur.prefix_sum+= valDiff
        self.hashmap[key]= val

    def sum(self, prefix: str) -> int:
        cur= self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur= cur.children[c]
        return cur.prefix_sum

