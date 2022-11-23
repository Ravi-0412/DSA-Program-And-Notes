# exactly same as 'longest substring with k unique char'
# only diff is there in condition: window size should contain all unique char
# which means window size should be equal to len(hashmap) 
# as no of unique char is given by the length of hashmap and we want all char unique in the window so for ans len(hashmap)== j-i+1 (window size)
# so only change is that replace k with window size i.e len(hashmap)== j-i+1

# agar window size len(hashmap) se bda h then it means repeating char is present in the window so start deleting the char from hashmap till len(hashmap) reaches to window size
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap,max_length,i,j,n= {},0,0,0,len(s)
        while j<n:
            hashmap[s[j]]= 1+ hashmap.get(s[j],0)
            if len(hashmap)== j-i+1:
                max_length= max(max_length,j-i+1)
            elif len(hashmap)< j-i+1:
                while len(hashmap)< j-i+1:
                    hashmap[s[i]]-= 1
                    if hashmap[s[i]]== 0:
                        hashmap.pop(s[i])
                        if len(hashmap)== j-i+1:
                            max_length= max(max_length,j-i)
                    i+= 1
            j+= 1
        print("longest substring is: ",s[i:j+1])
        return max_length

