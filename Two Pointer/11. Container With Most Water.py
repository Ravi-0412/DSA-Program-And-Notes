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

# Java Code
"""
//Method 1
import java.util.*;

class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int n = height.length;

        for (int l = 0; l < n; l++) {
            for (int r = l + 1; r < n; r++) {
                int curr_Area = (r - l) * Math.min(height[r], height[l]); // length * width
                maxArea = Math.max(maxArea, curr_Area);
            }
        }
        return maxArea;
    }
}
//Method 2
class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int l = 0, r = height.length - 1;  // For maximizing width

        while (l < r) {
            int curr_Area = (r - l) * Math.min(height[r], height[l]);
            maxArea = Math.max(maxArea, curr_Area);

            // Move the pointer with the smaller height
            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }
        }
        return maxArea;
    }
}
"""

# C++ Code
"""
//Method 1
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int n = height.size();

        for (int l = 0; l < n; l++) {
            for (int r = l + 1; r < n; r++) {
                int curr_Area = (r - l) * min(height[r], height[l]); // length * width
                maxArea = max(maxArea, curr_Area);
            }
        }
        return maxArea;
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int l = 0, r = height.size() - 1;  // For maximizing width

        while (l < r) {
            int curr_Area = (r - l) * min(height[r], height[l]);
            maxArea = max(maxArea, curr_Area);

            // Move the pointer with the smaller height
            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }
        }
        return maxArea;
    }
};
"""