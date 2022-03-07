# all five  approaches not working
class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        # i=0
        # while True:
        #     if (n& (pow(2,i)))==n:
        #         return i+1
        #         break
        #     i+= 1
        
        i=0
        while True:
            # idea of checking 2's comp from right
            if (n& (1<<i))!=n:  # if (n& (1<<i))==0:
                i+= 1
        return i+1
        
        # take '&' of the given number with 2's complement of the no
        # now all bits except the first set bit will become zero
        k= 0
        temp= n&-n
        while (temp>>k)!= 1:  # now do right shift till it becomes equal to '1'
            k+= 1
        # 'k+1' will give the ans
        return k+1

        # return int(math.log2 (n & -n)) + 1   
