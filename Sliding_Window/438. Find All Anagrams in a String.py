# submitted on leetcode
# how sliding window: har window size of len(p), chance h ki hmko ans mile

# logic: just store the count of each char of 'p' in dictionary
# jb koi letter mile jo hashmap me h , it means that letter is part of 'p' then decrement the count of that letter in dic by 1
# if count of that letter becomes zero means you have seen that letter in 's' the no of times that is present in 'p'
# in this case decr count by 1

# when 'j+1' reaches the len(p), there might be possiblity that window formed till now from 'i to j' in 's' may be part of 'anagram'
# so add index 'i' to the ans

# count: btayega ki tmhare pass kitne letter bache h jo or chahiye 'anagram' ke liye in proper no of occurence. count will tell the number of unique char that you need 
# count will be zero only when occurence of all ele in hashmap or say 'p' has become zero i.e means we have found all char in 'p' with no of times they are 'p' in string 's'
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i,j,hashmap= 0,0,{}
        for c in p:
	        hashmap[c]= 1+ hashmap.get(c,0)
        count, ans= len(hashmap),[]  # count is initialised to len(hashmap), it means itna diff char hmko khojna h and agar us char cahr ka count zero ho gya matlab ek char mil gya
	   # print(hashmap)    
        while(j<len(s)):
	        if s[j] in hashmap:
	            hashmap[s[j]] -= 1
	            if hashmap[s[j]]== 0:   # koi char gar jitn abar chahiye mil gya ho
	                count-= 1
	        if j+1>= len(p):     # or j-i+1== len(p)
	            if count== 0:    # matlab hmko sb char jitna bar chahiye tha utna bar mil gya h
	                ans.append(i)
				# for sliding the window, first check if condition satisfaying char is present at char 'i' like what we are searching for is present at 'i'
	            if s[i] in hashmap:
	                hashmap[s[i]]+= 1  # matlab is char ko itna bar hmko khojna hoga kyonki ab wo window me nhi h. actualy me hm 'i'th char ko window se nikla rhe h
	                if hashmap[s[i]]== 1:  # matlab ek ans wala char bahar hua h isliye hmko wo bhi khojna hoga and 
						# if removed char already present h window me i.e hashmap[s[i]] > 1 then hmko ans already present char h usse bhi mil sakta h isliye count nhi badhana h us case me
	                    count+= 1
	            i+= 1
	        j+= 1
        return ans  




# note: if you will simply check the length of hashmap at "j+1>= len(p)", then it will not work if char will be repeated in 'p' 
# since you will deleting the char in hash at 'i'th index in this approach