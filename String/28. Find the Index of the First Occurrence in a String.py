# Method 1: Brutre force

"""
Approach
1) Iterate through each possible starting position of needle in haystack.
2) For each starting position, check if the substring of haystack starting at that position matches needle.
3) If a match is found, return the starting index.
4) If no match is found after checking all possible positions, return -1.

time complexity : O((n-m+1)*m) where n is the length of haystack and m is the length of needle
"""

class Solution(object):
    def strStr(self, haystack, needle):
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        if len_needle == 0:
            return 0
        
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        
        return -1

# Java
"""
class Solution {
    public int strStr(String haystack, String needle) {
        int lenHaystack = haystack.length();
        int lenNeedle = needle.length();
        
        if (lenNeedle == 0) {
            return 0;
        }
        
        for (int i = 0; i <= lenHaystack - lenNeedle; i++) {
            if (haystack.substring(i, i + lenNeedle).equals(needle)) {
                return i;
            }
        }
        
        return -1;
    }
}
"""

# c++
"""
#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int lenHaystack = haystack.size();
        int lenNeedle = needle.size();
        
        if (lenNeedle == 0) {
            return 0;
        }
        
        for (int i = 0; i <= lenHaystack - lenNeedle; i++) {
            if (haystack.substr(i, lenNeedle) == needle) {
                return i;
            }
        }
        
        return -1;
    }
};
"""

# Method 2: Using 'Z- algo'.

# See the q: "2223. Sum of Scores of Built Strings" for detailed explanation.

# Time : O(m + n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m , n = len(haystack) , len(needle)
        # Make a new string combining both the string with one special character(to avoid comparison beyond that char)
        # jiska find karna h usko phle and jisme find karna h usko bad me.
        # Kyonki prefix == sufffix chahiye and jiska karna h wo prefix hona chahiye.
        s = needle + '$' + haystack   # any special symbol which is not allowed in string 
        # Now apply 'Z - Algo'.
        z = [0] * (m + n + 1)  # '1' for special symbol
        total = m + n + 1
        l , r = 0, 0
        for i in range(1, total):
            if i < r:
                z[i] = min(r -i , z[i - l])
            while i + z[i] < total and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l , r = i, i + z[i]
        # Now find the 1st index in 'z' for which z[i] == len(needle) that will be our ans.
        print(z)
        # only we need to check in string 'haystack' and that will start from 'n+1'.
        for i in range(n + 1, total):  
            if z[i] == n:  # len(needle)
                return i - n - 1  # then actual index in haystack will be excluding the len(needle) + 1(special symbol)
        return -1

# Java Code 
"""
class Solution {
    public int strStr(String haystack, String needle) {
        int m = haystack.length(), n = needle.length();
        if (n == 0) return 0; // Edge case for empty needle

        // Concatenate both strings with a special character to apply Z algorithm
        String s = needle + "$" + haystack;
        int total = m + n + 1;
        int[] z = new int[total];

        int l = 0, r = 0;
        for (int i = 1; i < total; i++) {
            if (i < r) {
                z[i] = Math.min(r - i, z[i - l]);
            }
            while (i + z[i] < total && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }

        // Find the first occurrence of needle in haystack
        for (int i = n + 1; i < total; i++) {
            if (z[i] == n) {
                return i - n - 1;
            }
        }

        return -1;
    }
}
"""

# C++ Code 
"""
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.size(), n = needle.size();
        if (n == 0) return 0; // Edge case for empty needle

        // Concatenate both strings with a special character to apply Z algorithm
        string s = needle + "$" + haystack;
        int total = m + n + 1;
        vector<int> z(total, 0);

        int l = 0, r = 0;
        for (int i = 1; i < total; i++) {
            if (i < r) {
                z[i] = min(r - i, z[i - l]);
            }
            while (i + z[i] < total && s[z[i]] == s[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }

        // Find the first occurrence of needle in haystack
        for (int i = n + 1; i < total; i++) {
            if (z[i] == n) {
                return i - n - 1;
            }
        }

        return -1;
    }
};
"""