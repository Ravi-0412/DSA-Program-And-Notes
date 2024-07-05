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

# java
"""
// Method 2:

public class Solution {
    public String multiply(String num1, String num2) {
        int len1 = num1.length();
        int len2 = num2.length();
        int[] ans = new int[len1 + len2];
        
        // Iterate over each digit in num1 and num2 starting from the least significant digit
        for (int i = len1 - 1; i >= 0; i--) {
            int carry = 0;
            for (int j = len2 - 1; j >= 0; j--) {
                // Calculate the total value at the current position
                int total = (num1.charAt(i) - '0') * (num2.charAt(j) - '0') + ans[i + j + 1] + carry;
                ans[i + j + 1] = total % 10;
                carry = total / 10;
            }
            // Add any remaining carry to the next position
            ans[i] += carry;
        }
        
        // Convert the result array to a string, skipping leading zeros
        StringBuilder result = new StringBuilder();
        for (int num : ans) {
            if (!(result.length() == 0 && num == 0)) {
                result.append(num);
            }
        }
        
        return result.length() == 0 ? "0" : result.toString();
    }
}
"""


# 1) if "0" in num1 or num2:  means if any of num1 or num2 will contain even a single zero then it will return the "0"
# 2) if "0" in [num1] or [num2]: it means if all char in array num1 or num2 is "0" then return  "0".
# 3) if "0" in [num1, num2]: just shorter way of writing the '2'.
