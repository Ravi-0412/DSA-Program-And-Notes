# just calculate the water trap at for each heights i. e
# Har level apne upper itna water store kar sakta..simple way to think of this q.
# summation of all the water trap will be ans width of each height= 1

# water trap for each heights= levels[i]- heights[i]  (have to subtract heights[i] for cal water trap above each height)
# and levels[i]= min(left_greatest[i], right_greatest[i]). 

# time: O(n)= space

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



# method 2: optimising the space to O(1), just same logic only
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
    

# java
"""
// Method 1:

class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] levels = new int[n];
        int[] leftGreatest = leftGreatest(height, n);
        int[] rightGreatest = rightGreatest(height, n);

        for (int i = 0; i < n; i++) {
            levels[i] = Math.min(leftGreatest[i], rightGreatest[i]) - height[i];
        }

        int totalWater = 0;
        for (int level : levels) {
            totalWater += level;
        }
        return totalWater;
    }

    private int[] leftGreatest(int[] height, int n) {
        int[] left = new int[n];
        left[0] = height[0];  // For the first element, the left greatest is the element itself
        for (int i = 1; i < n; i++) {
            left[i] = Math.max(left[i - 1], height[i]);  // Compare with previous one and update
        }
        return left;
    }

    private int[] rightGreatest(int[] height, int n) {
        // Same logic as above function, just traverse the array from right to left
        int[] right = new int[n];
        right[n - 1] = height[n - 1];  // For the last element, the right greatest is the element itself
        for (int i = n - 2; i >= 0; i--) {
            right[i] = Math.max(right[i + 1], height[i]);
        }
        return right;
    }
}

// Method 2:
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int l = 0, r = height.length - 1, n = height.length;
        int maxLeft = height[0], maxRight = height[n - 1];
        int ans = 0;

        while (l < r) {
            // Shift the minimum pointer and find the answer at the minimum pointer
            if (maxLeft > maxRight) {  // The water level is based on the right side (right bar is smaller)
                r--;
                maxRight = Math.max(maxRight, height[r]);
                ans += maxRight - height[r];
            } else {  // The water level is based on the left side (left bar is smaller)
                l++;
                maxLeft = Math.max(maxLeft, height[l]);
                ans += maxLeft - height[l];
            }
        }
        return ans;
    }
}


"""


# Similar questions asked in interviews:
# 1) https://www.csestack.org/snow-between-hills-coding-challenge/#google_vignette
