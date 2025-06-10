# Logic:
"""
Approach
Initialize Variables:
Use variables i and j to store the indices of characters that differ between the two strings. Initialize them to -1.
Use a counter cnt to count the number of differing positions.
Iterate Through the Strings:
Traverse each character of the strings using a loop.
If characters at the current position differ, increment the counter cnt.
Store the index of the differing characters in i and j when cnt is 1 and 2 respectively.
Check Conditions:
If cnt is 0, the strings are already equal, so return true.
If cnt is 2, check if swapping the characters at positions i and j in one string makes it equal to the other string.
If both conditions are met, return true; otherwise, return false.

# Time : O(n), space: O(1)
"""

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        i=-1
        j=-1
        cnt=0
        for k in range(0, len(s1)):
            if s1[k]!=s2[k]:
                cnt+=1
                if i==-1: i=k
                elif j==-1: j=k
        
        if cnt==0: return True
        elif cnt==2 and s1[i]==s2[j] and s1[j]==s2[i]: return True

        return False

# Java Code 
"""
class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int i = -1, j = -1, cnt = 0;

        for (int k = 0; k < s1.length(); k++) {
            if (s1.charAt(k) != s2.charAt(k)) {
                cnt++;
                if (i == -1) i = k;
                else if (j == -1) j = k;
            }
        }

        if (cnt == 0) return true;
        else if (cnt == 2 && s1.charAt(i) == s2.charAt(j) && s1.charAt(j) == s2.charAt(i)) return true;

        return false;
    }
}
"""

# C++ Code 
"""
#include <string>

using namespace std;

class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int i = -1, j = -1, cnt = 0;

        for (int k = 0; k < s1.size(); k++) {
            if (s1[k] != s2[k]) {
                cnt++;
                if (i == -1) i = k;
                else if (j == -1) j = k;
            }
        }

        if (cnt == 0) return true;
        else if (cnt == 2 && s1[i] == s2[j] && s1[j] == s2[i]) return true;

        return false;
    }
};
"""
