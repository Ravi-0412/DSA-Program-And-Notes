# Method 1 : Using Trie
# Time : O(n^2)
# Tle 

class TrieNode:
    def __init__(self):
        self.children= {}      # will point to children. and can be max of 26('a' to 'z').

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
    
    def search(self, word: str) -> bool:
        lcp = 0   # length of longest common prefix
        cur= self.root
        for c in word:
            if c not in cur.children:
                return lcp
            lcp += 1
            cur= cur.children[c]
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

# Logic: for each index > 0 and start comparing with index left = '0'  , right = i.
# For each index store the length such that prefix from index '0' == prefix starting from index 'i'.

# The Z-function for this string is an array of length n where the ith
# element is equal to the greatest number of characters starting from the position 'i' 
# that coincide with the first characters of 's'.

# z[i] : is the length of the longest string that is, at the same time, a prefix of 's' and
# a suffix of 's' starting at 'i'.

# Note : Here we are not making any extra string with 'special char'.
# We need to find by traversing in same string only.

# Time : O(n^2)

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        for i in range(1 , n):
            j , k = 0, i
            # for getting length from current index 'i', start comparing from 
            # prefix from index '0' and prefix starting from index 'i'.
            while k < n and s[j] == s[k]:
                j += 1
                k += 1
                z[i] += 1 
        return sum(z) + n    # given string will be contribute to ans so adding 'n'.
    

# other way of writing above code
# Logic: let's call 'segment matches' those substrings that coincide with a prefix of  's'.
# For example, the value of the desired Z-function
# z[i] is the length of the segment match starting at position
# i (and that ends at position (i + z[i] - 1).

# Time: O(n^2)

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        for i in range(1 , n):
            # just other way of above loop.
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        return sum(z) + n


# b) Modified one for Z function calculation
# Logic: 
# compute the values of z[i] in turn from i = 1 to n - 1 but at the same time, 
# when computing a new value, we'll try to make the best use possible of the previously computed values.

# Go through this for better understanding: https://cp-algorithms.com/string/z-function.html

# I have one doubt in :
# z[i] = min(r - i , z[i -l]) . why z[i - l] ?

# Time : O(n)

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        l , r = 0 ,0
        # l : last index till which we have computed the z-function.
        # r: index "boundary" to which our string 's' has been scanned by the algorithm, everything beyond that point is not yet known.
        for i in range(1 , n):
            if i < r :
                # the current position is inside the current segment match [l, r).

                # then no need to calculate from starting index '0'.
                # we can use the already calculated Z-values to "initialize" the value of z[i] 
                # to something (it is sure better than "starting from zero"), maybe even some big number.

                # min value of z[i] must be equal = z[i - l] but must be less than 'r - i' using prev computation.
                z[i] = min(r - i , z[i -l])
                # this will give the length of 'z[i]' before 'r' but can be more also.
            
            # if l >= r then z[i] = 0 till now
            
            # for calculating more(from r to n - 1) use the brute force logic (think like that only)
            # we need to only compare from index  'z[i]' on left(start) and 'i+ z[i]' on right.
            # if z[i] == 0 then it will automatically calculate from left = 0 and right = i
            while i + z[i] < n and s[z[i]]  == s[i + z[i]]:
                z[i] += 1
            # Now check if we can increase 'r' 
            # then update both 'l' and 'r'.
            if i + z[i] > r:
                # i to cur index and r = i + z[i]
                l, r = i , i + z[i]
        return sum(z) + n


# Note: Go through this link for better clarification and other question related to this.
# Link: https://cp-algorithms.com/string/z-function.html#efficient-algorithm-to-compute-the-z-function

# Other Applications of this algo:
# 1) Search the substring
# problem: we call 't' the string of text, and 'p' the pattern. 
# The problem is: find all occurrences of the pattern 'p' inside the text 't'.
    
# 2) Number of distinct substrings in a string
# Problem: Given a string  's' of length 'n' , count the number of distinct substrings of 's'.

# 3) String compression
# Problem: Given a string 's' of length 'n'.
# Find its shortest "compressed" representation, that is: find a string 't' of shortest length such that
# 's' can be represented as a concatenation of one or more copies of 't'.

# 4) Q: "https://leetcode.com/problems/subtree-of-another-tree/description/"

# Some more problem link is given inside above link.


