# BRute force: O(n^2)
# find the area between every pair of container and take the maximum
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

# Idea: 
# 1) The widest container (using first and last line) is a good candidate, because of its width.
# Its water level is the height of the smaller one of first and last line.
# 2) All other containers are less wide and thus would need a higher water level in order to hold more water.
# 3) The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

# So we can start from two end points and move the pointer for which height is less.
# From here we get idea of two pointer.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea= 0
        l,r= 0, len(height)-1   # for maximising the width
        while l<r :
            curr_Area= (r-l) * min(height[r], height[l])
            maxArea= max(maxArea, curr_Area)
            # move which is smaller since we are decreasing the width so we will try to move the smaller to get the bigger height.
            if height[l] > height[r]:   
                r-= 1
            else:  # can write above two into one
                l+= 1
        return maxArea

# java

"""
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int currentArea = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, currentArea);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
"""