class Solution:
    def reverse(self, x: int) -> int:
        # INTEGER.MAX_VALUE=  2147483647 (end with 7)
        # INTEGER.MIN_VALUE=  -2147483648 (end with -8 )
        
        MAX= 2147483647   # 2^31 - 1
        MIN= -2147483648  # -2^31
        res= 0
        while x:
            remainder= int(math.fmod(x, 10))   # (python dumb) -1 %  10 = 9.  that's why using 'fmod(x,y)' instead of "x % y".
            x= int(x/10)                        # (python dumb) -1 // 10 = -1
            # comparing with pre result so comparing with MAX(OR)MIN//10.
            if res> MAX//10 or (res== MAX//10 and remainder> MAX % 10):  # positive overflow
                return 0
            if res< MIN//10 or (res== MIN//10 and remainder< MIN % 10):  # negative overflow
                return 0
            res= res*10 + remainder
        return res

# same logic but very concise.
# just keep on reversing and keep on checking the overflow.
class Solution:
    def reverse(self, x: int) -> int:
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
