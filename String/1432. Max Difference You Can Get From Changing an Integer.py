# lOGIC: 
"""
We need to maximize the difference of two numbers a and b. Therefore we should maximize a and minimize b.

To maximize a we need to find the left-most digit in it that is not a 9 and replace all occurences of that digit with 9.
9 is the maximum possible digit and the more left we find a candidate for replacement the bigger the result gets.

To minimize b we need to find the left-most digit in it that is not a 0 and replace all occurences of that digit with 0.
But we have to watch out: We are not allowed to convert the first digit to a '0' as we should not create a number with trailing zeroes.
Therefore we can only replace the first digit with a 1. All other digits can be replaced with a 0 if they are not a 1 as that 
would also replace the trailing 1 with a 0.

# time: O(d), where d is the number of digits in num.
"""

class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = str(num)

        # find the left-most digit in it that is not a 9 and replace all occurences of that digit with 9.
        for digit in a:
            if digit != "9":
                # replace all occurence of 'digit' with '9'.
                a = a.replace(digit, "9")       
                break
        
        if b[0] != "1":
            # then for getting minimum it is better to replace all occurence of digit 'b[0]' with '1'
            # because in this case you cn't replace with '0' as '0' can't come at start.
            b = b.replace(b[0], "1")
        else:
            # if first digit is '1' then replace the first digit which is not 0/1 from left with zero.
            for digit in b[1:]:
                if digit not in "01":
                    b = b.replace(digit, "0")
                    break
        
        return int(a) - int(b)
    
# Java Code
"""
class Solution {
    public int maxDiff(int num) {
        String a = String.valueOf(num), b = String.valueOf(num);

        // find the left-most digit in it that is not a 9 and replace all occurrences of that digit with 9.
        for (char digit : a.toCharArray()) {
            if (digit != '9') {
                // replace all occurrences of 'digit' with '9'.
                a = a.replace(digit, '9');
                break;
            }
        }

        if (b.charAt(0) != '1') {
            // then for getting minimum it is better to replace all occurrences of digit 'b[0]' with '1'
            // because in this case you can't replace with '0' as '0' can't come at start.
            b = b.replace(b.charAt(0), '1');
        } else {
            // if first digit is '1' then replace the first digit which is not 0/1 from left with zero.
            for (int i = 1; i < b.length(); i++) {
                if (b.charAt(i) != '0' && b.charAt(i) != '1') {
                    b = b.replace(b.charAt(i), '0');
                    break;
                }
            }
        }

        return Integer.parseInt(a) - Integer.parseInt(b);
    }
}
"""

# C++ Code
"""
#include <string>

using namespace std;

class Solution {
public:
    int maxDiff(int num) {
        string a = to_string(num), b = to_string(num);

        // find the left-most digit in it that is not a 9 and replace all occurrences of that digit with 9.
        for (char digit : a) {
            if (digit != '9') {
                // replace all occurrences of 'digit' with '9'.
                replace(a.begin(), a.end(), digit, '9');
                break;
            }
        }

        if (b[0] != '1') {
            // then for getting minimum it is better to replace all occurrences of digit 'b[0]' with '1'
            // because in this case you can't replace with '0' as '0' can't come at start.
            replace(b.begin(), b.end(), b[0], '1');
        } else {
            // if first digit is '1' then replace the first digit which is not 0/1 from left with zero.
            for (size_t i = 1; i < b.size(); i++) {
                if (b[i] != '0' && b[i] != '1') {
                    replace(b.begin(), b.end(), b[i], '0');
                    break;
                }
            }
        }

        return stoi(a) - stoi(b);
    }
};
"""
