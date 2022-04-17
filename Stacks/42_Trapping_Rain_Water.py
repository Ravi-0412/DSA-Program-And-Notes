# just calculate the water trap at for each heights
# water trap for each heights= levels[i]- heights[i]  (have to sub heights[i] for cal water trap above each height)
# and levels[i]= min(left_greatest[i], right_greatest[i]) as any heights can't store water above this level
# summation of all the water trap will be as width of each height= 1
# time: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        levels= [0]*n
        left_greatest=  self.LeftGreatest(height, n)
        right_greatest= self.RightGreatest(height, n)
        for i in range(n):
            levels[i]= min(left_greatest[i], right_greatest[i])- height[i]
        return sum(levels)
    
    def LeftGreatest(self,height,n):
        # here in case of no left greatest exist we write the arr[i] in the ans instead of '-1'
        # since it can store water upto that level
        # this is the only diff bw the q that i solved 'replace every ele with left greatest' and this Q
        # so only need to compare with the previous ele and max of both will go into the ans
        left= [0]*n
        left[0]= height[0]  # for 1st ele, left greatest will be the that ele itself
        for i in range(1,n):
            left[i]= max(left[i-1],height[i])  # compare with pre one and update 
        return left
    
    def RightGreatest(self,height,n):
        # same logic as above fn, just traverse the array from right to left
        right= [0]*n
        right[n-1]= height[n-1]     # for last ele, right greatest will be the that ele itself
        for i in range(n-2,-1,-1):
            right[i]= max(right[i+1],height[i])
        return right

# We can solve within one function itself, just use the for loop
# think of other concise and space: o(1) solution
# other methods in pass and concise one have to see later from gf and leetcode discussion link