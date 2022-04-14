# exactly same as 'longest substring with k unique char'
# only diff is there in condition: window size should contain all unique char
# which means window size should be equal to len(hashmap) for any of the ans
# as no of unique char is given by the length of hashmap and we want all char unique in the window
# so only chabge is that replace k with window size i.e len(hashmap)== j-i+1
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

