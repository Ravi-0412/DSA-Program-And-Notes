# method 1: using the inbuilt function to convert decimal into binary
# then count the number of '1'
# submitted on GFG
# time: O(n)

class Solution:
    	def setBits(self, N):
	        return bin(N).replace("ob","").count('1')

# method 2: (submitted on leetcode)
# just check the rightmost bit using bitwise operator and count
# time: O(1), as we have to check only 32 bit

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):
            if n&1==1:
                count+= 1
            n>>= 1
        return count

# method3: submitted on leetcode
# it execute only to the no of set bits  
# Logic: as n is formed from 'n-1' by changing one bit and so on every iteration one '1' will get cancelled out when we will take '&',
# as while taking add and updating, the value tends towards zero very fast as bits changes.
# time: o(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):    
            count+= 1
            # temp= n & n-1   # take and with its pre no 
            # n= temp         # update the value of n= result of '&' operation and repeat till n becomes zero
            n= n & n-1    # concise way of writing abobe two lines    
        return count      # no of times loop will execute that will give the ans

