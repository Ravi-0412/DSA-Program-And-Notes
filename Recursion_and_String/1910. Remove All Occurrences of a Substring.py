# Itertaion.
# time: will be in O(m*n) but difficult to find the exact as after removing 'part' from 's', s can again form 'part' so.
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        p= len(part)
        while part in s:
            i= s.index(part)      # find the index where part is present in 's'.
            s= s[:i] + s[i+ p :]  # remove the part from the 's'.
        return s
# Java
"""
class Solution {
    public String removeOccurrences(String s, String part) {
        while (s.contains(part)) {
            int i = s.indexOf(part); // Find the index where 'part' is present in 's'.
            s = s.substring(0, i) + s.substring(i + part.length()); // Remove the 'part' from 's'.
        }
        return s;
    }
}
"""

# just converted the above logic into recursion.
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        i= s.index(part)      # find the index where part is present in 's'.
        s= s[: i] + s[i+ len(part) :]  # remove the part from the 's'.
        return self.removeOccurrences(s, part)
        

# Later try in O(m+n) using KMP.
