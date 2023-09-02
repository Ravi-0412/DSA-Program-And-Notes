# Method 1 : Using Trie

class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').
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
    
    def search(self, word: str) -> bool:
        lcp = 0   # length of longest common prefix
        cur= self.root
        for c in word:
            if c not in cur.children:
                return lcp
            lcp += 1
            cur= cur.children[c]
        # now we have traversed all the char of 'word' so if 'cur.isEndOfWord== True' then it means this word is present otherwise not.
        return lcp

class Solution:
    def sumScores(self, s: str) -> int:
        trie = Trie()
        trie.insert(s)
        ans = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            ans += trie.search(s[i : n])
        return ans


# Method 2: Z- Algo

# Intuition: Each s_i is a suffix of the string s, so consider algorithms that can determine the longest prefix that is also a suffix.
# from this we can think of using 'Z-Algo'.

# a) Brute force

# Logic: for each index start comparing with index left = '0'  , right = 0.

# Note : Here we are not making any extra string with 'special char'.
# We need to find traverse in same string only.

# Time : O(n^2)

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        for i in range(1 , n):
            j , k = 0, i
            while k < n and s[j] == s[k]:
                j += 1
                k += 1
                z[i] += 1 
        return sum(z) + n    # given string will be contribute to ans so adding 'n'.


# b) Modified one for Z function calculation
# Time : O(m + n)

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        l , r = 0 ,0  
        for i in range(1 , n):
            if i < r :
                # then no need to calculate from starting index '0'
                # min value of z[i] must be equal = z[i - l] but must be less than 'r' using prev computation.
                z[i] = min(r - i , z[i -l])
                # this will give the length of 'z[i]' before 'r' but can be more also.
            # if l >= r then z[i] = 0 till now
            # for calculating more(from r to n - 1) use the brute force logic (think like that only)
            # we need to only compare from index  'i' on left and 'i+ z[i]' on right.
            # if z[i] == 0 then it will automatically calculate from left = 0 and right = i
            while i + z[i] < n and s[z[i]]  == s[i + z[i]]:
                z[i] += 1
            # Now check if we increase 'r' 
            # then update both 'l' and 'r'.
            if i + z[i] > r:
                # i to cur index and r = i + z[i]
                l, r = i , i + z[i]
        return sum(z) + n


# See the String Telegram channel notes and video for better visualisation.


