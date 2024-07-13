# similar logic to "find anargam"

# Logic: First find a valid window in which all char of 't' is present in s.
# then compress the window size if possible to decrease the size of the ans subarray.
# so when count becomes == 0(means we have found all char of t in proper quantity) 
# then try to compress if possible by incr 'i' keeping 'j' constant.
# Note: compression is only possible if any char is present extra time in window than the required or 'not required char' is present.

# 'count' will tell how many we have not seen till now in proper quantity.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        hashmap= {}
        for c in t:
	        hashmap[c]= 1+ hashmap.get(c,0)  
        n= len(s)
        minLen, ans= n +1, ""
        count= len(hashmap)
        i, j= 0, 0
        while j< len(s):
            if s[j] in hashmap:
	            hashmap[s[j]] -= 1  # ek bar is char ko dekhe
	            if hashmap[s[j]]== 0:   # koi char gar jitn abar chahiye mil gya ho
	                count-= 1
            # in case if count becomes zero, means we have found one subarray
            # till count== 0 means all char in at least in proper quantity in that subarray. so keep updating the ans
            while count== 0:  
                # first update the ans
                if minLen > j-i+1:   # means got new better ans
                    minLen= j-i+1
                    ans= s[i:j+1]
                # now try to shrink the window by  
                if s[i] in hashmap:   
                    hashmap[s[i]]+= 1  # then we have to search this char again in upcoming window this much time (if negative then already in extra amount in cur window itself) 
                    # if it becomes = 1 means thic char is not present in extra quantity anymore. so incr the count
                    if hashmap[s[i]]== 1:    
                        count+= 1  # means we have to find this char in proper
                # else that char more in quantity than required or was not part of 't' so we can shrink the window 
                i+= 1  # keep shrinking till count==0 means till we are having valid subarray
            j+= 1
        return ans


# Java
""""
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public String minWindow(String s, String t) {
        if (t.length() > s.length()) {
            return "";
        }

        Map<Character, Integer> hashmap = new HashMap<>();
        for (char c : t.toCharArray()) {
            hashmap.put(c, hashmap.getOrDefault(c, 0) + 1);
        }

        int n = s.length();
        int minLen = n + 1;
        String ans = "";
        int count = hashmap.size();
        int i = 0, j = 0;

        while (j < s.length()) {
            if (hashmap.containsKey(s.charAt(j))) {
                hashmap.put(s.charAt(j), hashmap.get(s.charAt(j)) - 1);
                if (hashmap.get(s.charAt(j)) == 0) {
                    count--;
                }
            }

            while (count == 0) {
                if (minLen > j - i + 1) {
                    minLen = j - i + 1;
                    ans = s.substring(i, j + 1);
                }

                if (hashmap.containsKey(s.charAt(i))) {
                    hashmap.put(s.charAt(i), hashmap.get(s.charAt(i)) + 1);
                    if (hashmap.get(s.charAt(i)) == 1) {
                        count++;
                    }
                }
                i++;
            }
            j++;
        }

        return ans;
    }
}

"""

# similar q
# 1) Smallest subarray with sum greater than x