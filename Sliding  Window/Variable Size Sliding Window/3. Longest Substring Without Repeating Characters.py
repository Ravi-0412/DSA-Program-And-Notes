# Similar as as 'longest substring with k unique char' 
# only diff is there in condition: 'window size should contain all unique char'
# which means window size should be equal to len(hashmap).
# as no of unique char is given by the length of hashmap and 
# we want all char unique in the window so for ans len(hashmap)== j-i+1 (window size)
# so only change is that replace k with window size i.e len(hashmap)== j-i+1 & change the size from '>' to '<'.

# agar window size len(hashmap) se bda h then it means repeating char is present in the window 
# so start deleting the char from hashmap till len(hashmap) reaches to window size

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap, max_length, i, j, n= {}, 0, 0, 0, len(s)
        while j < n:
            hashmap[s[j]]= 1+ hashmap.get(s[j],0)   
            while len(hashmap) < j-i+1:   # it can only happen if window contain duplicate char
                hashmap[s[i]]-= 1
                if hashmap[s[i]]== 0:
                    del hashmap[s[i]]
                i+= 1
            max_length= max(max_length, j - i + 1)
            j+= 1
        # print("longest substring is: ",s[i: j+1])
        return max_length


# Java.
"""
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> hashmap = new HashMap<>();
        int maxLength = 0;
        int i = 0, j = 0, n = s.length();

        while (j < n) {
            hashmap.put(s.charAt(j), hashmap.getOrDefault(s.charAt(j), 0) + 1);

            while (hashmap.size() < j - i + 1) { // it can only happen if window contains duplicate char
                hashmap.put(s.charAt(i), hashmap.get(s.charAt(i)) - 1);
                if (hashmap.get(s.charAt(i)) == 0) {
                    hashmap.remove(s.charAt(i));
                }
                i++;
            }

            maxLength = Math.max(maxLength, j - i + 1);
            j++;
        }

        return maxLength;
    }
}
"""