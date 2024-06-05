# Just same questions as: "2131. Longest Palindrome by Concatenating Two Letter Words".

class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        freq = collections.defaultdict(int)
        ans = 0
        for c in s:
            if freq[c] > 0:
                ans += 2
                freq[c] -= 1
            else:
                freq[c] += 1
        for key, value in freq.items():
            if value > 0:
                ans += 1
                break
        return ans


# Java
"""
class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        int ans = 0;
        for(int i = 0; i < s.length() ; i ++) {
            if(freq.containsKey(s.charAt(i)) && freq.get(s.charAt(i)) > 0 ) {
                ans += 2;
                int f = freq.get(s.charAt(i)) ;
                freq.put(s.charAt(i), f -1);
            }
            else {
                freq.put(s.charAt(i), 1) ;
            }
        }
        for(Map.Entry<Character,Integer> entry : freq.entrySet()) {
            if(entry.getValue() > 0) {
                ans += 1 ;
                break; 
            }
        }
        return ans ;        
    }
}
"""