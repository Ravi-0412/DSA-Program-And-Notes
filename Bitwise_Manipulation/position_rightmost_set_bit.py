
# logic 1st method: just check when rightmost bit becomes 1 by right shifting the number and taking '&' with '1'.

class Solution:
    def getFirstSetBit(self,n):
        count= 0
        while n >0:
            count+= 1
            if (n &1): # first bit can also be the set bit
                return count
            else:
                n= n>>1
        return 0


# another way of writing 1st method:
def getFirstSetBit(self,n):
        i=0
        while n>0:
            if (n& (pow(2,i)))== pow(2,i):  # simply finding first time from right when no becomes of the form '2^n'.
                return i+1
            i+= 1
        return 0


# 2nd method: if we somehow make all the bits on the left side of the 1st one equal to zero and all right bit equal to zero 
# and we if take 'And' all bit on left and right side of 1st set bit will become equal to zero.
# then the no of bits in the resulting number will be the ans

# for this ,only thing come into mind is to find the two's complement amd then take '&' and then take log

# Note: when we write '-' before any number then that will get converted to 2's complement of the given no 
# and '~' gives one's complement when written with some other number & operator(^, |, &&)

# e.g: 476. Number Complement 
# have to find 1's complement and if you will just return '~num' then it won't work because elements are stored in 2's complement form.

# logic: (n&~(n-1)) always return the binary number containing the rightmost set bit as 1. if N = 12 (1100) then it will return 4 (100).
# And the returned binary number will be of power of '2'.
# So just find the power value using log and add '1'.
import math
class Solution:
    def getFirstSetBit(self,n):
        return int(math.log2(n & ~(n-1))) + 1 if n!=0 else 0


# Method 3: Best and concise
# logic: # just the logic we find the two's complement i.e start from right and after you see first one then just change 0->1 and 1->0

# return int(math.log2(n & -n)) + 1 if n!=0 else 0      # best and concise
        