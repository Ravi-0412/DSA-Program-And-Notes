# Note: Input is passed as a Integer only

class Solution:
    def reverseBits(self, n: int) -> int:
        ans= 0
        for i in range(32):
            rightMostBit= (n >> i) & 1
            # now we have to move this bit to the left
            # after that to keep this bit at left like if 0->0 and  1->1 keeping all the other bit same we will take OR with the ans
            ans= ans | rightMostBit<<(31-i)  # to this position we have to move the bit 
        return ans
