# Logic: While traversing each word we have to match it with pre seen 'word'
# having same freq count of each ele (i.e anargam).

# Method 1:
# just used the meaning of anargam like when sorted they should be same.
# time: O(m*n*logn)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)    # sorted : return list so converting into tuple because list can't be key.
        return hashmap.values()


# Method 2: 

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

# Java
"""
// method 1:

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);
            
            if (!map.containsKey(sortedWord)) {
                map.put(sortedWord, new ArrayList<>());
            }
            
            map.get(sortedWord).add(word);
        }
        
        return new ArrayList<>(map.values());
    }
}

// method 2:

    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) return new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] ca = new char[26];
            for (char c : s.toCharArray()) ca[c - 'a']++;
            String keyStr = String.valueOf(ca);   # take the value of 'ca' array and convert the values into single string and make this string as key
            if (!map.containsKey(keyStr)) map.put(keyStr, new ArrayList<>());
            map.get(keyStr).add(s);
        }
        return new ArrayList<>(map.values());
    }
"""