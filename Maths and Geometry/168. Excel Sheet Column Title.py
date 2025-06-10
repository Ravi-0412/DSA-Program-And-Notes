# Method 1: 

# Excel sheet column no title :
# [A,B,...Z], [AA,AB,....,AZ], [BA,BB,...,BZ],....[ZA,ZB,....,ZZ],[AAA,AAB,....,AAZ],.......

# consider the letter 'A' to have a value of 1, 'B'->2 ..... 'Z'->26
# note that in the above notation, values are 1-based
# here our Radix (R) == 26
# the final value of a number 'X Y Z' = X * R^2 + Y * R + Z  
# Note: Just conversion of number from base '26' to decimal.

# this looks similar to base-10 decimal number but the biggest difference is that the 
# numbers on every digit starts with 1, instead of 0., and the max on each digit goes up to R (Radix) instead of R-1

# for example
# Z== Radix = 26
# then next number is AA = R + 1 = Z+1
# ZZ = R * R + R
# next number is AAA = 1*R^2 + 1 * R + 1 = ZZ +1

# Logic: 
# The goal of this problem is to convert base10 system to base26 system.
# Excel sheet base26 system is represented by the 26 capital letters. 
# Note this system has no concept of 0. Similar to Roman numerals, where 0 does not exist i.e X = 10,  XI = 11.

# Excel sheet title: It is like in a number system in which after 9 it is 00 instead of 10; 
# or like a system without zero: starting with 1, 2.. and after 9 it is 11.

# Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

# But how to get the column title from the number? We can't simply use the n%26 method because:

# ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

# We can use (n-1)%26 instead, then we get a number range from 0 to 25.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        colToChar = {0: 'Z', 1 : 'A', 2: 'B', 3: 'C', 4: 'D',5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
                     11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
                     20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

        ans = ""
        while columnNumber > 26:
            r = columnNumber % 26
            ans = colToChar[r] + ans  # keep adding this 'r' title to the front
            columnNumber = columnNumber // 26 if r != 0 else columnNumber // 26 - 1   # to handle cases like "52" and multiple of 'z'.
        ans = colToChar[columnNumber] + ans
        return ans
    

# My mistake at start:
# 1) 
# This will not work if 'columnNumber' is multiple of '26'.
# Because for '0' there is no matching char.

# Time : O(log26^n) , space : O(26)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        colToChar = {1 : 'A', 2: 'B', 3: 'C', 4: 'D',5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
                     11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
                     20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

        ans = ""
        while columnNumber > 26:
            r = columnNumber % 26
            ans = colToChar[r] + ans
            columnNumber = columnNumber // 26
        ans = colToChar[columnNumber] + ans
        return ans

# Other way of writing same above logic
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 26:
            columnNumber , r = divmod(columnNumber, 26)
            if r == 0:
                ans = "Z" + ans
            else:
                c = chr(r + 65 - 1)
                ans = c + ans
        return chr(columnNumber + 65 - 1) + ans


# Method 2:
# Very better one. Handling corner cases of method '1' very good.
# Time : O(log26^n) , space : O(26)
class Solution:
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])  # array in '0' based indexing so doing '-1'.
            num = (num-1) // 26
        return ''.join(result[::-1])

# Method 3: 
# Most optimised
# Time : O(log26^n) , space : O(1)
class Solution:
    def convertToTitle(self, num):
        result = []
        while num > 0:
            cur = (num - 1) % 26
            result.append(chr(cur + ord('A'))) 
            num = (num - 1) // 26
        return ''.join(result[::-1])
        
# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public String convertToTitle(int columnNumber) {
        Map<Integer, Character> colToChar = new HashMap<>();
        colToChar.put(0, 'Z');
        for (int i = 1; i <= 26; i++) {
            colToChar.put(i, (char) ('A' + i - 1));
        }

        StringBuilder ans = new StringBuilder();
        while (columnNumber > 26) {
            int r = columnNumber % 26;
            ans.insert(0, colToChar.get(r));
            columnNumber = (r != 0) ? columnNumber / 26 : columnNumber / 26 - 1;
        }
        ans.insert(0, colToChar.get(columnNumber));
        return ans.toString();
    }
}
//Method 2
class Solution {
    public String convertToTitle(int num) {
        char[] capitals = new char[26];
        for (int i = 0; i < 26; i++) {
            capitals[i] = (char) ('A' + i);
        }

        StringBuilder result = new StringBuilder();
        while (num > 0) {
            result.insert(0, capitals[(num - 1) % 26]);
            num = (num - 1) / 26;
        }
        return result.toString();
    }
}
//Method 3
class Solution {
    public String convertToTitle(int num) {
        StringBuilder result = new StringBuilder();
        while (num > 0) {
            int cur = (num - 1) % 26;
            result.insert(0, (char) (cur + 'A'));
            num = (num - 1) / 26;
        }
        return result.toString();
    }
}
"""

# C++ Code 
"""
//Method 1
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        unordered_map<int, char> colToChar = {
            {0, 'Z'}, {1, 'A'}, {2, 'B'}, {3, 'C'}, {4, 'D'}, {5, 'E'}, {6, 'F'}, {7, 'G'}, {8, 'H'}, {9, 'I'}, {10, 'J'},
            {11, 'K'}, {12, 'L'}, {13, 'M'}, {14, 'N'}, {15, 'O'}, {16, 'P'}, {17, 'Q'}, {18, 'R'}, {19, 'S'},
            {20, 'T'}, {21, 'U'}, {22, 'V'}, {23, 'W'}, {24, 'X'}, {25, 'Y'}, {26, 'Z'}
        };

        string ans = "";
        while (columnNumber > 26) {
            int r = columnNumber % 26;
            ans = colToChar[r] + ans;
            columnNumber = (r != 0) ? columnNumber / 26 : columnNumber / 26 - 1;
        }
        ans = colToChar[columnNumber] + ans;
        return ans;
    }
};
//Method 2
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string convertToTitle(int num) {
        vector<char> capitals;
        for (char c = 'A'; c <= 'Z'; c++) {
            capitals.push_back(c);
        }

        string result = "";
        while (num > 0) {
            result = capitals[(num - 1) % 26] + result;
            num = (num - 1) / 26;
        }
        return result;
    }
};
//Method 3
#include <string>

using namespace std;

class Solution {
public:
    string convertToTitle(int num) {
        string result = "";
        while (num > 0) {
            int cur = (num - 1) % 26;
            result = char(cur + 'A') + result;
            num = (num - 1) / 26;
        }
        return result;
    }
};
"""