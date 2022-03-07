# method 1: using the inbuilt function to convert decimal into binary
# then count the number of '1'
# submitted on GFG
# time: O(n)

class Solution:
    	def setBits(self, N):
	        return bin(N).replace("ob","").count('1')

# method 2: (submitted on leetcode)
# just check the rightmost bit using bitwise operator and count
# time: O(logn)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):
            if n&1==1:
                count+= 1
            n>>= 1
        return count


