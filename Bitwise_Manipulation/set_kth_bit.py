# for setting we always use 'OR' with '1'
# and for reset we use 'AND' with '0'
# for getting one at kth position do left shift '1'
# 'k' time(if last bit start from zero)
# after that take 'OR'

# submitted on GFG
class Solution:
    def setKthBit(self, N, K):
	    return (N |(1<< K))   # 'k' times since start with zero

