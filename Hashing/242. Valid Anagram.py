"""
The Anagram "Golden Rule": Two strings are anagrams if and only if they have the same characters with the same frequencies. 
Sorting (O(n *log n)) is the easiest to write, but Hash Maps (O(n)) are the fastest to run.
"""


# method 1: 
# Note: Anargam is just another meaning of permutation.
# Means 1) both 's' and 't' should have equal length 
# 2) all char should be present in same frequency 
# Logic: When we sort any two permutation then, both should be same.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)== sorted(t)


# Method 2:
# Permutation also means:
# 1) both 's' and 't' should have equal length 
# 2) all char should be present in same frequency 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s , counter_t = Counter(s), Counter(t)
        for c in s:
            if c not in  counter_t or counter_s[c] != counter_t[c]:
                return False
        return True

# Method 3:

# time= space= O(m + n), sapce : O(m)
# logic: just we find all anargams of a given string.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap= {}
        for c in s:
            hashmap[c]= 1+ hashmap.get(c, 0)
        count= len(hashmap)
        for c in t:
            # not checking 2nd condition will give error. Because if freq[c] = 0 then we are not deleting the ele only decr the count.
            # e.g: s= "nagaram", t= "anagramm"
            if c not in hashmap or hashmap[c] <= 0:  
                return False
            hashmap[c]-= 1
            if hashmap[c]==0:
                count-= 1
        return count== 0

"""
Follow up : Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

If the strings contain Unicode (like Emojis or different languages), your Hash Map approach is already the best choice.

Hash Map : A dictionary in Python handles any hashable character. 
Whether it's 'a', 'ñ', or '🚀', the logic remains exactly the same. No changes needed!
"""

