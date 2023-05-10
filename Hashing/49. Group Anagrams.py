# same method as we find all anargams.
# time: O(m*n*26). m: #words, n: # char in each word.
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)
        for s in strs:
            count= [0]*26   # to store the count of each char for each string.   a.....z
            for c in s:
                count[ord(c)- ord("a")]+= 1
            # append all string with these number of char count as key.
            # changing into tuple because list can't be key.
            hashmap[tuple(count)].append(s)    
        return hashmap.values()

# just used the meaning of anargam like when sorted they should be same.
time: O(m*n*logn)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)    # append all string with thse number of char count
        return hashmap.values()

