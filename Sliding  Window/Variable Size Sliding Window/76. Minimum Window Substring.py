# similar logic to "find anargam"
# here we have to compress the window size if possible to decrease the size of the ans subarray.
# so when count becomes == 0 then try to compress if possible by incr 'i' keeping 'j' constant.
# compression is only possible if any char is present extra time in window than the required

# differences from "find anargam"
# here no necessary to increase the 'i' always after j-i+1== len(t) as here the char in 't' may not be continous. 
# in "find anargam" all the char should be continous so we will always have to incr 'i' after j-i+1== len(t)

# so first find any window that contain all char of 't' at least in proper quantity then try to shrink the window if possible.

# while shrinking the window only incr 'i' if we can get better ans otherwise don't incr 'i' 
# i.e first reach the count==0 then only try to incr the 'i' if shrinking is possible.

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
