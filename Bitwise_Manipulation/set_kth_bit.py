# for setting we always use 'OR' with '1' at that position i.e keep 1 at that position and 
# keep '0' at all other position i.e or the given number by 2^k
# and for reset we use 'AND' with '0'
# for getting one at kth position do left shift '1'
# 'k' time(if last bit start from zero)
# after that take 'OR'

# submitted on GFG
class Solution:
    def setKthBit(self, N, K):
	    return (N |(1<< K))   # 'k' times since start with zero

