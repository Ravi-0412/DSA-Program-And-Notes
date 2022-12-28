# method 1: 'Anargam' means when we sort them, they should be same.(another meaning than permutation).
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)== sorted(t)

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

