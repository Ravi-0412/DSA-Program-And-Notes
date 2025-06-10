# Explanation:
# a in prefix is good, skip all a in the beginning.
# If all characters are a, change the last char to z.
# From the first char not a, decrese them, until next a.

# time: O(n), space: O(n)

class Solution:
    def smallestString(self, s: str) -> str:
        n= len(s)
        s= list(s)   # we can't change in string so first converting into list.
        i= 0
        # skip all a in the beginning because it is already smallest lexographically till now.
        while i  < n and s[i] == 'a':
            i += 1
        # If all characters are a, change the last char to z. Because we have to perform at exacyly one operation so change the last one.
        # and for 'a' we will change to 'z' only.
        if i == n:
            s[n-1]= 'z'
            return "".join(s)
        # Now to get the smallest we will start decreasing  from first non_a char till we will find next 'a' 
        # because if we include 'a' also then it will become bigger as 'a' will change to 'z'.
        while i < n and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i += 1
        return "".join(s)

# Java Code 
"""
class Solution {
    public String smallestString(String s) {
        int n = s.length();
        char[] arr = s.toCharArray();
        int i = 0;

        // Skip all 'a' characters at the beginning
        while (i < n && arr[i] == 'a') {
            i++;
        }

        // If all characters are 'a', change the last one to 'z'
        if (i == n) {
            arr[n - 1] = 'z';
            return new String(arr);
        }

        // Start decreasing from the first non-'a' character until we find the next 'a'
        while (i < n && arr[i] != 'a') {
            arr[i] = (char) (arr[i] - 1);
            i++;
        }

        return new String(arr);
    }
}
"""

# C++ Code 
"""
#include <string>

using namespace std;

class Solution {
public:
    string smallestString(string s) {
        int n = s.size();
        int i = 0;

        // Skip all 'a' characters at the beginning
        while (i < n && s[i] == 'a') {
            i++;
        }

        // If all characters are 'a', change the last one to 'z'
        if (i == n) {
            s[n - 1] = 'z';
            return s;
        }

        // Start decreasing from the first non-'a' character until we find the next 'a'
        while (i < n && s[i] != 'a') {
            s[i] = s[i] - 1;
            i++;
        }

        return s;
    }
};
"""

