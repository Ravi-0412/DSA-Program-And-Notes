# submitted on leetcode
# logic in  notes
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i,j,hashmap= 0,0,{}
        for c in p:
	        hashmap[c]= 1+ hashmap.get(c,0)
        count, ans= len(hashmap),[]
	   # print(hashmap)    
        while(j<len(s)):
	        if s[j] in hashmap:
	            hashmap[s[j]] -= 1
	            if hashmap[s[j]]== 0:
	                count-= 1
	        if j-i+1 < len(p):
	            j+= 1
	        elif j-i+1== len(p):
	            if count== 0:
	                ans.append(i)
	            if s[i] in hashmap:
	                hashmap[s[i]]+= 1
	                if hashmap[s[i]]== 1:
	                    count+= 1
	            i+= 1
	            j+= 1
        return ans  


# submitted on gfg
class Solution:
    	def search(self,pat, txt):
	    i,j,hashmap= 0,0,{}
	    for c in pat:
	        hashmap[c]= 1+ hashmap.get(c,0)
	    count, ans= len(hashmap),0
	   # print(hashmap)    
	    while(j<len(txt)):
	       if txt[j] in hashmap:
	           hashmap[txt[j]] -= 1
	           if hashmap[txt[j]]== 0:
	               count-= 1
	       if j-i+1 < len(pat):
	           j+= 1
	       elif j-i+1== len(pat):
	           #print(hashmap)
	           #print("hii",count)
	           if count== 0:
	               ans= ans+1
	           if txt[i] in hashmap:
	               hashmap[txt[i]]+= 1
	               if hashmap[txt[i]]== 1:
	                   count+= 1
	           i+= 1
	           j+= 1
	    return ans

