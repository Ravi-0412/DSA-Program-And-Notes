# BRute force: O(n^2)
# find the area between every container and take the maximum
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea= 0
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                curr_Area= (r-l) * min(height[r], height[l])   # length*width
                maxArea= max(maxArea, curr_Area)
        return maxArea


# time: O(n)
# using two pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea= 0
        l,r= 0, len(height)-1   # for maximising the width
        while l<r :
            curr_Area= (r-l) * min(height[r], height[l])
            maxArea= max(maxArea, curr_Area)
            if height[l] > height[r]:   # move which is smaller since we are decreasing the width so we will try to move the smaller
                r-= 1
            # elif height[l] < height[r]:
            #     l+= 1
            # else:  # can move nay of one
            #     l+= 1

            else:  # can write above two into one
                l+= 1
        return maxArea

# logic behind moving 'l' and 'r': simple thought we have to move so that we can get larger area
# when ai < aj, if we move j to the left:
# 1. the length on x-axis will definitly decrease
# 2. if a(j-1) > ai, the area will be ai * length on x-axis which is smaller than original area
# 3. if a(j-1) < ai, the area will be a(j-1) * length on x-axis which is also smaller than original area
# so moving j to the left won't give us a larger area, we can only move i to the right to get a possible larger area.


