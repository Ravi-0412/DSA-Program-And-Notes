# submitted on leetcode
# anargam: is same like permutation only . meaning: har char hmko proper quantitity me chahiye that's it and same what permutation means
# how sliding window: har window size of len(p), chance h ki hmko ans mile

# logic: just store the count of each char of 'p' in dictionary
# jb koi letter mile jo hashmap me h , it means that letter is part of 'p' then decrement the count of that letter in dic by 1
# if count of that letter becomes zero means you have seen that letter in 's' the no of times that is present in 'p'
# in this case decr count by 1
# actually me count 'no of distinct char' bta rha.

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
        while(j<len(s)):
	        if s[j] in hashmap:
	            hashmap[s[j]] -= 1   # this may go negative also means we have seen extra s[j] than required and this will help in upcoming window since we will have already these ele present
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
		


# Note: ye fixed sliding window isliye h ki hmko har char proper quantity me chahiye together i.e hmko char window size= len(p)
# me ans check karna hoga.

# Java
""""

public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int i = 0, j = 0;
        Map<Character, Integer> hashmap = new HashMap<>();
        for (char c : p.toCharArray()) {
            hashmap.put(c, hashmap.getOrDefault(c, 0) + 1);
        }
        int count = hashmap.size();
        List<Integer> ans = new ArrayList<>();
        
        while (j < s.length()) {
            if (hashmap.containsKey(s.charAt(j))) {
                hashmap.put(s.charAt(j), hashmap.get(s.charAt(j)) - 1);
                if (hashmap.get(s.charAt(j)) == 0) {
                    count--;
                }
            }
            
            if (j + 1 >= p.length()) {
                if (count == 0) {
                    ans.add(i);
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