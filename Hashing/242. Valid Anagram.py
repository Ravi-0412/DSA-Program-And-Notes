# Note: Anargam is just another meaning of permutation.
# Means 1) both 's' and 't' should have equal length 
# 2) all char should be present in same frequency 

# method 1: 
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
            if c not in t or counter_s[c] != counter_t[c]:
                return False
        return True

# Method 3:

# time= space= O(n)
# logic: just we find all anargams of a given string.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap= {}
        for c in s:
            hashmap[c]= 1+ hashmap.get(c, 0)
        count= len(hashmap)
        for c in t:
            if c not in s:
                return False
            hashmap[c]-= 1
            if hashmap[c]==0:
                count-= 1
        return count== 0

