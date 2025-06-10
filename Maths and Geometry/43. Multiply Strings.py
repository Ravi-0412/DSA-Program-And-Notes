# just conversion of logic we do the multiplication normally.
# nOte: when we multiply two number then no of digit in answer can't go beyond 'len(num1) + len(num2)'.
# time: O(m*n)
# space: O(m+ n)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if "0" in [num1] or "0" in [num2]:
        #     return "0"
        if "0" in [num1, num2]: return "0"  # concise way of writing above
        len1, len2= len(num1), len(num2)
        ans= [0]*(len1 + len2)
        num1, num2= num1[::-1], num2[::-1]  # revrsing to do multiplication left to right.
        for i1 in range(len1):
            for i2 in range(len2):
                digit= int(num1[i1]) * int(num2[i2])
                ans[i1 + i2]+= digit # directly add no matter single digit number or double digit number as carry for next will be given from here.
                                     # we have to add with already values of this position.
                # forward if carry to the next position in the ans'
                ans[i1+ i2+ 1]+= ans[i1 + i2] //10   # ading if any carry
                # now update the ans for current position
                ans[i1 + i2]= ans[i1 + i2]%10   

        # ans will be in reverse order. so 1st we have to reverse then remove the '0' from the left and then return the ans
        ans, beg= ans[::-1], 0
        while beg < len(ans) and ans[beg]== 0:
            beg+= 1
        return "".join(str(e) for e in ans[beg:])
    

# Method 2: Just we do multiplication 
# i.e from right to left. No need to reverse
# Note: if we multiply two index 'i1' and 'i2' then it's value will at : 'i1 + i2 + 1' 
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1] or "0" in [num2]:
            return "0"
        len1, len2= len(num1), len(num2)
        ans= [0] *(len1 + len2)
        for i1 in range(len1 - 1, -1, -1):
            carry = 0
            for i2 in range(len2 - 1 , -1, -1):
                # calculate the total value we will get at index 'i1 + i2 + 1' 
                total = int(num1[i1]) * int(num2[i2]) + ans[i1 + i2 + 1] + carry
                digit , carry = total % 10 , total // 10
                ans[i1 + i2 + 1] = digit
            # if carry then add the carry value one index ahead. 
            if carry > 0 :
                ans[i1] += carry   
        return "".join(str(e) for e in ans).lstrip("0")

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0"; // concise way of checking for zero

        int len1 = num1.length(), len2 = num2.length();
        int[] ans = new int[len1 + len2];
        StringBuilder result = new StringBuilder();

        for (int i1 = len1 - 1; i1 >= 0; i1--) {
            int carry = 0;
            for (int i2 = len2 - 1; i2 >= 0; i2--) {
                int total = (num1.charAt(i1) - '0') * (num2.charAt(i2) - '0') + ans[i1 + i2 + 1] + carry;
                ans[i1 + i2 + 1] = total % 10;
                carry = total / 10;
            }
            if (carry > 0) ans[i1] += carry;
        }

        for (int e : ans) {
            if (!(result.length() == 0 && e == 0)) result.append(e);
        }
        return result.length() == 0 ? "0" : result.toString();
    }
}
//Method 2
class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";

        int len1 = num1.length(), len2 = num2.length();
        int[] ans = new int[len1 + len2];

        for (int i1 = len1 - 1; i1 >= 0; i1--) {
            int carry = 0;
            for (int i2 = len2 - 1; i2 >= 0; i2--) {
                int total = (num1.charAt(i1) - '0') * (num2.charAt(i2) - '0') + ans[i1 + i2 + 1] + carry;
                ans[i1 + i2 + 1] = total % 10;
                carry = total / 10;
            }
            if (carry > 0) ans[i1] += carry;
        }

        StringBuilder result = new StringBuilder();
        for (int e : ans) {
            if (!(result.length() == 0 && e == 0)) result.append(e);
        }
        return result.length() == 0 ? "0" : result.toString();
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
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0"; // concise way of checking for zero

        int len1 = num1.size(), len2 = num2.size();
        vector<int> ans(len1 + len2, 0);
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end()); // reversing to do multiplication left to right

        for (int i1 = 0; i1 < len1; i1++) {
            for (int i2 = 0; i2 < len2; i2++) {
                int digit = (num1[i1] - '0') * (num2[i2] - '0');
                ans[i1 + i2] += digit; // directly add, carry will be handled in the next step
                ans[i1 + i2 + 1] += ans[i1 + i2] / 10; // forwarding carry to the next position
                ans[i1 + i2] %= 10; // updating the current position
            }
        }

        reverse(ans.begin(), ans.end());
        int beg = 0;
        while (beg < ans.size() && ans[beg] == 0) beg++; // removing leading zeros

        string result;
        for (int i = beg; i < ans.size(); i++) {
            result += to_string(ans[i]);
        }
        return result;
    }
};
//Method 2
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int len1 = num1.size(), len2 = num2.size();
        vector<int> ans(len1 + len2, 0);

        for (int i1 = len1 - 1; i1 >= 0; i1--) {
            int carry = 0;
            for (int i2 = len2 - 1; i2 >= 0; i2--) {
                int total = (num1[i1] - '0') * (num2[i2] - '0') + ans[i1 + i2 + 1] + carry;
                ans[i1 + i2 + 1] = total % 10;
                carry = total / 10;
            }
            if (carry > 0) ans[i1] += carry;
        }

        string result;
        for (int e : ans) {
            if (!(result.empty() && e == 0)) result += to_string(e);
        }
        return result.empty() ? "0" : result;
    }
};
"""

# 1) if "0" in num1 or num2:  means if any of num1 or num2 will contain even a single zero then it will return the "0"
# 2) if "0" in [num1] or [num2]: it means if all char in array num1 or num2 is "0" then return  "0".
# 3) if "0" in [num1, num2]: just shorter way of writing the '2'.
