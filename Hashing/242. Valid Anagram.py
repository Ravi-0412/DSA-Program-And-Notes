# Note: Anargam is just another meaning of permutation.
# Means 1) both 's' and 't' should have equal length 
# 2) all char should be present in same frequency 

# method 1: 
# Logic: When we sort any two permutation then, both should be same.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)== sorted(t)


# Method 2:
# Permutation also means:
# 1) both 's' and 't' should have equal length 
# 2) all char should be present in same frequency 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s , counter_t = Counter(s), Counter(t)
        for c in s:
            if c not in t or counter_s[c] != counter_t[c]:
                return False
        return True

# Method 3:

# time= space= O(n)
# logic: just we find all anargams of a given string.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap= {}
        for c in s:
            hashmap[c]= 1+ hashmap.get(c, 0)
        count= len(hashmap)
        for c in t:
            # not checking 2nd condition will give error. Because if freq[c] = 0 then we are not deleting the ele only decr the count.
            # e.g: s= "nagaram", t= "anagramm"
            if c not in s or hashmap[c] <= 0:  
                return False
            hashmap[c]-= 1
            if hashmap[c]==0:
                count-= 1
        return count== 0


# Java
"""
# method 1: 
# Logic: When we sort any two permutation then, both should be same.

import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        // Convert strings to character arrays and sort them
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        
        // Compare sorted arrays
        return Arrays.equals(sChars, tChars);
    }
}
"""

"""
# Method 2:
# Permutation also means:
# 1) both 's' and 't' should have equal length 
# 2) all char should be present in same frequency 

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create hashmaps to store character counts
        Map<Character, Integer> counterS = new HashMap<>();
        Map<Character, Integer> counterT = new HashMap<>();
        
        // Count characters in strings s and t
        for (char c : s.toCharArray()) {
            counterS.put(c, counterS.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            counterT.put(c, counterT.getOrDefault(c, 0) + 1);
        }
        
        // Check if character counts are equal
        for (char c : s.toCharArray()) {
            if (!counterT.containsKey(c) || !counterS.get(c).equals(counterT.get(c))) {
                return false;
            }
        }
        return true;
    }
}

// other way

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> count = new HashMap<>();
        for(char x: s.toCharArray()) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }
        for(char x: t.toCharArray()) {
            count.put(x, count.getOrDefault(x, 0) - 1);
        }
        for(int val: count.values()){
            if(val != 0){
                return false;
            }
        }
        return true;
        
    }
}

"""


"""
# time= space= O(n)
# logic: just we find all anargams of a given string.

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> hashmap = new HashMap<>();
        
        // Count characters in string s
        for (char c : s.toCharArray()) {
            hashmap.put(c, hashmap.getOrDefault(c, 0) + 1);
        }
        
        int count = hashmap.size(); // Count of unique characters
        
        // Iterate through string t
        for (char c : t.toCharArray()) {
            if (!hashmap.containsKey(c) || hashmap.get(c) <= 0) {
                return false; // Character in t not found in s, hence not an anagram
            }
            
            hashmap.put(c, hashmap.get(c) - 1); // Decrement count of character
            
            if (hashmap.get(c) == 0) {
                count--; // Decrease count of unique characters if count of current character becomes 0
            }
        }
        
        return count == 0; // If count becomes 0, all characters in s have been matched and it's an anagram
    }
}



"""