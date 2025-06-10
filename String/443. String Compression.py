# Method 1: 
class Solution:
    def compress(self, chars: List[str]) -> int:
        AnsIndex= 0
        i =0
        while i  < len(chars):
            curChar, count = chars[i], 0
            while i < len(chars) and chars[i] == curChar:
                i+= 1
                count+= 1
            # first append the char
            chars[AnsIndex] = curChar
            AnsIndex += 1 
            # now append its count if count > 1.
            if count > 1:
                # if count >= 10 then that should be written like '1', '0'.
                for c in str(count):
                    chars[AnsIndex] = c
                    AnsIndex += 1
        return AnsIndex
        # return len(chars) # will give incorrect ans as chars will be diff but compiler is automatically modifying char till our ans.


# If asked for only length of compressed string given no need to modify the original chars array.
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0
        while i  < len(chars):
            curChar, count= chars[i], 0
            while i < len(chars) and chars[i] == curChar:
                i+= 1
                count+= 1
            # first incr for appending char
            ans += 1
            # now append its count if count > 1.
            if count > 1:
                ans += len(str(count))
        return ans

# Java
"""
//Method 1
import java.util.*;

class Solution {
    public int compress(char[] chars) {
        int AnsIndex = 0;
        int i = 0;
        while (i < chars.length) {
            char curChar = chars[i];
            int count = 0;
            while (i < chars.length && chars[i] == curChar) {
                i++;
                count++;
            }
            // first append the char
            chars[AnsIndex] = curChar;
            AnsIndex += 1;
            // now append its count if count > 1.
            if (count > 1) {
                // if count >= 10 then that should be written like '1', '0'.
                for (char c : String.valueOf(count).toCharArray()) {
                    chars[AnsIndex] = c;
                    AnsIndex += 1;
                }
            }
        }
        return AnsIndex;
        // return chars.length; // will give incorrect ans as chars will be diff but compiler is automatically modifying char till our ans.
    }
}

// If asked for only length of compressed string given no need to modify the original chars array.
class Solution {
    public int compress(char[] chars) {
        int ans = 0;
        int i = 0;
        while (i < chars.length) {
            char curChar = chars[i];
            int count = 0;
            while (i < chars.length && chars[i] == curChar) {
                i++;
                count++;
            }
            // first incr for appending char
            ans += 1;
            // now append its count if count > 1.
            if (count > 1) {
                ans += String.valueOf(count).length();
            }
        }
        return ans;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int AnsIndex = 0;
        int i = 0;
        while (i < chars.size()) {
            char curChar = chars[i], count = 0;
            while (i < chars.size() && chars[i] == curChar) {
                i++;
                count++;
            }
            // first append the char
            chars[AnsIndex] = curChar;
            AnsIndex += 1;
            // now append its count if count > 1.
            if (count > 1) {
                // if count >= 10 then that should be written like '1', '0'.
                for (char c : to_string(count)) {
                    chars[AnsIndex] = c;
                    AnsIndex += 1;
                }
            }
        }
        return AnsIndex;
        // return chars.size(); // will give incorrect ans as chars will be diff but compiler is automatically modifying char till our ans.
    }
};


// If asked for only length of compressed string given no need to modify the original chars array.
class Solution {
public:
    int compress(vector<char>& chars) {
        int ans = 0;
        int i = 0;
        while (i < chars.size()) {
            char curChar = chars[i], count = 0;
            while (i < chars.size() && chars[i] == curChar) {
                i++;
                count++;
            }
            // first incr for appending char
            ans += 1;
            // now append its count if count > 1.
            if (count > 1) {
                ans += to_string(count).length();
            }
        }
        return ans;
    }
};
"""
