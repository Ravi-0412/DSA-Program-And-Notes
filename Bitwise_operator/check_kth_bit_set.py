# submitted on gfg
# index start from 0 from LSB
class Solution: 
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        if ((n & (1<< k)) >> k)==0:
            return False
        return True
