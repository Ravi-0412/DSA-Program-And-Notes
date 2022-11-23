# similar logic to "find anargam"
# here we have to compress the window size if possible so when count becomes == 0 then try to compress if possible by incr 'i' keeping 'j' constant
# compression is only possible if any char is present extra time in window than the required

# differences from "find anargam"
# here no necessary to increase the 'i' always after j-i+1== len(t) as here the char in 't' may be continous. 
# so first find any window that contain all of 't' in exact number then try to shrink the window if possible, 
# while shrinking the window only incr 'i' otherwise don't incr 'i' i.e first reach the count==0 then only try to incr the 'i' if shrinking is possible
# in "find anargam" all the char should be continous so we will always have to incr 'i' after j-i+1== len(t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        i,j,hashmap= 0,0,{}
        minLen, ans= 999999, ""
        for c in t:
	        hashmap[c]= 1+ hashmap.get(c,0)  
        count, ans= len(hashmap),""
        while j< len(s):
            if s[j] in hashmap:
	            hashmap[s[j]] -= 1
	            if hashmap[s[j]]== 0:   # koi char gar jitn abar chahiye mil gya ho
	                count-= 1
            while count== 0:
                if minLen > j-i+1:   # means got new better ans
                    minLen= j-i+1
                    ans= s[i:j+1]
                if s[i] in hashmap:
                    hashmap[s[i]]+= 1
                    if hashmap[s[i]]== 1:
                        count+= 1 
                i+= 1
            j+= 1
        return ans