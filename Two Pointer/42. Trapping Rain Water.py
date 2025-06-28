# Method 1: 

# just calculate the water trap at for each heights i. e
# Har level apne upper itna water store kar sakta..simple way to think of this q.
# summation of all the water trap will be ans width of each height= 1

# water trap for each heights= levels[i]- heights[i]  (have to subtract heights[i] for cal water trap above each height)
# and levels[i]= min(left_greatest[i], right_greatest[i]). 

# time: O(n)= space

"""
Similar questions asked in interviews:
1) https://www.csestack.org/snow-between-hills-coding-challenge/#google_vignette
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        levels= [0]*n
        left_greatest=  self.LeftGreatest(height, n)
        right_greatest= self.RightGreatest(height, n)
        for i in range(n):
            levels[i]= min(left_greatest[i], right_greatest[i]) - height[i]
        return sum(levels)
    
    def LeftGreatest(self,height,n):
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
            right[i]= max(right[i+1], height[i])
        return right



# method 2: 
# optimising the space to O(1), just same logic only
# very nicee logic: may be very helpful in other problems also

# logic: we need GreatestLeft and GreatestRight for each level
# so we can keep two pointer left and right for this 
# keep two variable for storing maxLeft and maxRight. 

# soo nicee logic.. keep this in mind

class Solution:
    def trap(self, height: List[int]) -> int: 
        if not height: return 0
        l,r, n= 0, len(height)-1, len(height)
        maxLeft, maxRight= height[0], height[n-1]
        ans= 0
        while l < r:
            # shift the minimum pointer and find the ans at minimum pointer
            if maxLeft > maxRight:  # then at 'r-1' we can store max water according to its maxRight one
                # it means the water level is based on the right side (the right bar is smaller) then move right side.
                r -= 1  
                maxRight = max(maxRight, height[r])
                ans += maxRight - height[r]
            else:  # then at 'l' it can store max water according to its maxLeft minimum one
                # it means the water level is based on the left side (the left bar is smaller) then move left side
                l+= 1
                maxLeft = max(maxLeft, height[l])
                ans += maxLeft- height[l]
        return ans
    



