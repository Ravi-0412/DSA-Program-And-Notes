# method 1: apply the logic of counting set bits with "n= n & n-1".

# method 2:
# write down in notebook you will get this pattern for even and odd number.
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans= [0]*(n+1)
        for num in range(1, n+1):
            if num %2 ==0:
                ans[num]= ans[num//2]
            else: 
                ans[num]= ans[num-1] +1   # or ans[num]= ans[num//2] +1
        return ans
