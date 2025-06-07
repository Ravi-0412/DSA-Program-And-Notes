#method 1 : 2 pointers

# logic: traverse both simultaneoulsy and when both char is same incr both pointer else incr pointer of 't' only(say 'j').

# 'i' will tell the no of char of 's' that we seen in 't' at any point of time.

# At last if value of 'i' >= len(s) means we have got all char of 's' in 't'.
#apporach : 
#1) start 2 variables i and j,both are initializes to 0 , which points s and t respectively
#2)in this while loop both the points runs upto the lenth of the strings ,
#in this loop if s[i] == t[j], move both forward (i++, j++).
#If characters don’t match, move only j++ to keep looking for a match for s[i] in t.
#after the loop , If all characters of s were matched (i == len(s)), return True.
#Otherwise, return False (some characters in s weren’t found in order in t).
# time: O(m + n)
# space :O(1)

#Python code :
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j= 0, 0  # will point to 's' and 't' respectively
        while i < len(s) and j < len(t):
            if s[i]== t[j] :
                i+= 1
                j+= 1
            else:
                j+= 1 
        return i== len(s)  # means we have got all c
   
#C++ code :
"""
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;  // will point to 's' and 't' respectively
        while (i < s.size() && j < t.size()) {
            if (s[i] == t[j]) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        return i == s.size();  // means we have matched all characters of 's'
    }
};
"""
#Java code :
"""
class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;  // will point to 's' and 't' respectively
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        return i == s.length();  // means we have matched all characters of 's'
    }
}
"""
    

#method 2 :Recursion
#Apporach 
#1)write a helper function (isSubseq), for recurssion logic.in this fuction If the current characters of s and t match, move both pointers one step left and recurse.
#If they don't match, move only the pointer in t one step left and recurse.
#in this fuction their must be present base condition If the length of string s becomes 0, it means all characters of s are matched , means empty string → return true.
#If t becomes 0 but s still has unmatched characters → return false.
#2)Now in the main function Start by calling the helper function with the full lengths of s and t and
# the result of this recursive check determines whether s is a subsequence of t.
#Time complexity : O(n)
#Space complexity : O(n)

#python code : 
class Solution:
    def isSubSeq(self, str1, str2, m, n):
        if m == 0:
            return True
        if n == 0:
            return False
        if str1[m - 1] == str2[n - 1]:
            return self.isSubSeq(str1, str2, m - 1, n - 1)
        return self.isSubSeq(str1, str2, m, n - 1)

    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        return self.isSubSeq(s, t, m, n)

# C++ code :
"""
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isSubSeq(string str1, string str2, int m, int n) {
        if (m == 0) return true;  // All characters of 's' matched
        if (n == 0) return false; // 't' exhausted before 's' was fully matched
        
        if (str1[m - 1] == str2[n - 1]) {
            return isSubSeq(str1, str2, m - 1, n - 1);
        }
        return isSubSeq(str1, str2, m, n - 1);
    }

    bool isSubsequence(string s, string t) {
        return isSubSeq(s, t, s.size(), t.size());
    }
};
"""

# Java code : 
"""
class Solution {
    public boolean isSubSeq(String str1, String str2, int m, int n) {
        if (m == 0) return true;  // All characters of 's' matched
        if (n == 0) return false; // 't' exhausted before 's' was fully matched
        
        if (str1.charAt(m - 1) == str2.charAt(n - 1)) {
            return isSubSeq(str1, str2, m - 1, n - 1);
        }
        return isSubSeq(str1, str2, m, n - 1);
    }

    public boolean isSubsequence(String s, String t) {
        return isSubSeq(s, t, s.length(), t.length());
    }
}
"""
