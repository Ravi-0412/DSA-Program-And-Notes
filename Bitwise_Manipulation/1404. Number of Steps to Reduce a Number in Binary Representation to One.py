# Method 1:
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s,2)
        ans = 0
        while num != 1:
            if num & 1 :
                num += 1
            else:
                num //= 2
            ans += 1
        return ans


# But above logic won't work in java/ c ++
# because maximum length of 's' can be = 500
# which can't be stored in either int or long.

# This wil give : "NumberFormatException" for larger input.
"""
class Solution {
    public int numSteps(String s) {
        long num = Integer.parseInt(s, 2);
        int ans = 0;
        while (num != 1) {
            if ((num & 1) == 1) {
                num += 1;
            } else {
                num /= 2;
            }
            ans += 1;
        }
        return ans;
    }
}
"""

# So somehow we will have to find answer without conversion only.

# Method 2:
# Logic: 1) go each digit from right side .
# Take carry = 0 initially
# 2) Add the current index val with carry, there will be three possibility after addition:
# a) result = 0 => in this case we need only '1' operation i.e  divide by '2'. carry will become '0' in this case.
# b) result = 1 => in this case we will need two operation i.e first add '1' and then divide by '2'. In this case carry = 1
# b) result = 2 => in this case we will need one operation i.e divide by '2'. In this case carry = 1

# And for leftmost digit , it will depend on carry .
# if carry  = 1 then add '1' else '0'.   e.g: "11"
# if carry = 1 then then no need to any operation on last digit.
# if carry == 1 then it will give sum = 2 so we need one operation i.e divide by '2'.
# so final ans = ans + carry

class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s) - 1
        carry = 0
        count = 0
        while (l > 0):
            ##even number with carry = 0, result even
            if int(s[l]) + carry == 0:
                carry = 0
                count += 1
            
            # even number with carry = 1, result odd
            # odd number with carry = 0, result odd
            elif int(s[l]) + carry == 1 :
                carry = 1
                count += 2
            #odd number with carry = 1, result even
            else:
                carry = 1
                count += 1
            l -= 1
        return count + carry


# Java
""""
class Solution {
    public int numSteps(String s) {
        int l = s.length() - 1;
        int carry = 0;
        int count = 0;
        while (l > 0) {
            int digit = Character.getNumericValue(s.charAt(l));
            if (digit + carry == 0) {
                // Even number with carry = 0, result even
                carry = 0;
                count += 1;
            } else if (digit + carry == 1) {
                // Even number with carry = 1, result odd
                // Odd number with carry = 0, result odd
                carry = 1;
                count += 2;
            } else {
                // Odd number with carry = 1, result even
                carry = 1;
                count += 1;
            }
            l -= 1;
        }
        return count + carry;
    }
}

"""


# Method 3:
# combining 1st and 3rd 'if' condition.

# No need to reset carry = 1 when 'int(s[l]) + carry == 0' because once carry is set no way we can get ''int(s[l]) + carry == 0'.
# And also when 'int(s[l]) + carry == 2', we need to set the carry = 1 but for this carry need to set before to get sum = 2 .
# So we only need to set carry = 1 when 'int(s[l]) + carry == 1' and later this carry will move ahead.

class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s) - 1
        carry = 0
        count = 0
        while (l > 0):
            #  0 + 1 = 1 odd, need  two steps (add 1 and divided by 2), (carry = 1)
            #  1 + 0 = 1 odd, need  two steps (add 1 and divided by 2), (carry = 0)
            if int(s[l]) + carry == 1:
                carry = 1
                count += 2
            else:
                #  0 + 0 = 0 even, need one step(divided by 2), (carry = 0)
                #  1 + 1 = 0 even, need one step(divided by 2), (carry = 1 ,  carry keeps 1 in next round.)
                count += 1
            l -= 1
        return count + carry


# in java
"""
class Solution {
    public int numSteps(String s) {
        int res = 0, carry = 0;
        for (int i = s.length() - 1; i > 0; --i) {
            // 0 + 1 = 1 odd, need  two steps (add 1 and divided by 2), (carry = 1)
            // 1 + 0 = 1 odd, need  two steps (add 1 and divided by 2), (carry = 0)
            if (s.charAt(i) - '0' + carry == 1) {
                carry = 1;
                res += 2;
            } else
                // 0 + 0 = 0 even, need one step(divided by 2), (carry = 0)
                // 1 + 1 = 0 even, need one step(divided by 2), (carry = 1 ,  carry keeps 1 in next round.)
                res += 1;
        }
        return res + carry;
    }
}
"""