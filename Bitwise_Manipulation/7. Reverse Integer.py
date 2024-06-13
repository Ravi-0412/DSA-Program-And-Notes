# Method 1:
# Just convert number into positive and apply normal reverse method.
class Solution:
    def reverse(self, x: int) -> int:
        dir = 1
        if x < 0:
            dir = -1
            x = -x
        MAX= (1 << 31) - 1  # 2^31 - 1
        res = 0
        while x:
            remainder =  x % 10                  
            res = res*10 + remainder
            x = x  // 10                 
            # checking overflow
            if res > MAX:
                return 0  
        return res if dir > 0 else -1*res


# Method 2: 
# just keep on reversing and keep on checking the overflow.
class Solution:
    def reverse(self, x: int) -> int:
        # INTEGER.MAX_VALUE=  2147483647 (end with 7)
        # INTEGER.MIN_VALUE=  -2147483648 (end with -8 )

        MAX= 2147483647   # 2^31 - 1
        MIN= -2147483648  # -2^31
        res= 0
        while x:
            remainder= int(math.fmod(x, 10))   # (python dumb) -1 %  10 = 9.  that's why using 'fmod(x,y)' instead of "x % y".
            res= res*10 + remainder
            x= int(x/10)                        # (python dumb) -1 // 10 = -1
            # checking overflow
            if res> MAX or res < MIN:
                return 0  
        return res


# java
"""
// why 'if ((newResult - tail) / 10 != result)' is handling the overflow.
in case of overflow, you won't get result from new result because roll over in case of overflow happens very uniquely.

public static void main(String[] args) {
    int rollMeOver= Integer.MAX_VALUE + 1;
    System.out.println(rollMeOver);
}
=> You will get as an output -2147483648 which represents the lowest value for an integer (Integer.MIN_VALUE).

class Solution {
    public int reverse(int x) {
        int result = 0;

        while (x != 0)
        {
            int tail = x % 10;
            int newResult = result * 10 + tail;
            if ((newResult - tail) / 10 != result)
            { return 0; }
            result = newResult;
            x = x / 10;
        }

        return result;
        }
}
"""