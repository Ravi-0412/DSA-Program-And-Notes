# just calculate the water trap at for each heights
# water trap for each heights= levels[i]- heights[i]  (have to subtract heights[i] for cal water trap above each height)
# and levels[i]= min(left_greatest[i], right_greatest[i]). Har level apne upper itna water store kar sakta..simple way to think of this q
# summation of all the water trap will be as width of each height= 1
# time: O(n)= space

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



# method 2: optimising the space to O(1), just same logic only
# very nicee logic: may be very helpful in other problems also

# logic: we need GreatestLeft and GreatestRight for each level
# so we can keep two pointer left and right for this 
# keep two variable for storing maxLeft and maxRight
# VVI: when you are standing at any level then you might think we know about maxLeft or maxRight only 
# but it is not necessary that right pointer wil be GreatestRight or left pointer will be Greatestleft
# yeah that's correct that right pointer may not give the GreatestRight and sam efor left but we need only min(maxLeft, maxRight) and
# if maxLeft is smaller than ele at right pointer then it must be lesser than the GreatestRight and same for right.. so we don't need to care about that 

# soo nicee logic.. keep this in mind
# https://www.youtube.com/watch?v=ZI2z5pq0TqA
class Solution:
    def trap(self, height: List[int]) -> int: 
        if not height: return 0
        l,r, n= 0, len(height)-1, len(height)
        maxLeft, maxRight= height[0], height[n-1]
        ans= 0
        while l <r:
            # shift the minimum pointer and find the ans at minimum pointer
            if maxLeft > maxRight:  # then at 'r' it can store max water according to its maxRight minimum one
                r-= 1
                maxRight= max(maxRight, height[r])
                ans+= maxRight- height[r]
            else:  # then at 'l' it can store max water according to its maxLeft minimum one
                l+= 1
                maxLeft= max(maxLeft, height[l])
                ans+= maxLeft- height[l]
        return ans