
# submitted on GFG(12/06/2022)
# logic 1st method: just check when rightmost bit becomes 1 by right shifting the number and taking '&' with '1'
# 2nd method: if we somehow make all the bits on the left side of the 1st one equal to zero and all right bit equal to zero 
# and we if take 'And' all bit on left side of 1st set bit will become equal to zero
# then the no of bits in the resulting number will be the ans

# for this only thing come into mind is to find the two's complement amd then take '&' and then take log

class Solution:
    def getFirstSetBit(self,n):
        count= 0
        while n >0:
            count+= 1
            if (n &1): # first bit can also be the set bit
                return count
                break
            else:
                n= n>>1
        return 0

        # return int(math.log2(n & -n)) + 1 if n!=0 else 0      # best and concise


# another way of writing 1st method:
def getFirstSetBit(self,n):
        i=0
        while n>0:
            if (n& (pow(2,i)))== pow(2,i): 
                return i+1
                break
            i+= 1
        return 0


