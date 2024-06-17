# we only need to check till sqrt(c).

# Note: 0 is also valid, and these two numbers can be the same.

# Logic: for doing on pen and paper
# if any prime factor of given number gives remainder '3' when divided
# by '4' && their power is odd then sum of square is not possible.
# Note: All such prime should have even power only.

# When even we can combine all such number with other number or in themselves to make as one of square 
# which is not possible in case any power is even.

# e.g: 2450 is given by 2450 = 2 * 5^2 * 7^2. 
# In this only '7' is such factor (when divided by 4 will give remainder 3) but it has even power
# so it is possible to write: 2450 = 7^2 + 49^2.  

# e.g: 588: 2^2 * 3 * 7^2
# here '3' and '7' both are such number only(will give remainder 3 when divided by 4)
# but '3' has odd power so we can't write like that.

# Note: There can be more than one way possible.
# e.g:  2450 = 7^2 + 49^2 OR 35^2 + 35^2

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(sqrt(c))
        while i <= j:
            if i**2 + j **2 == c:
                return True
            if i**2 + j **2 > c:
                j -= 1
            else:
                i += 1
        return False


# java
"""
// int can overflow(> 2^31 - 1) while calculating sum of square so used long. 
class Solution {
    public boolean judgeSquareSum(int c) {
        long i = 0, j = (long) Math.sqrt(c);
        while (i <= j) {
            long sum = i * i + j * j;
            if (sum == c) {
                return true;
            } else if (sum > c) {
                j--;
            } else {
                i++;
            }
        }
        return false;
    }
}
"""